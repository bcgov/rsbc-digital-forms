#!/usr/bin/env python3
"""
Script to generate SQL UPSERT statements for the lki_segment table
from a CSV file.
"""

import csv
import os
import sys
import argparse
from pathlib import Path


def generate_upsert_sql(csv_file_path: str, output_sql_path: str) -> None:
    """
    Generate UPSERT SQL statements for the lki_segment table from CSV data.

    Args:
        csv_file_path: Path to the input CSV file
        output_sql_path: Path to write the output SQL file
    """
    if not os.path.exists(csv_file_path):
        print(f"Error: CSV file not found at {csv_file_path}")
        sys.exit(1)

    sql_statements = []
    sql_statements.append("-- UPSERT statements for lki_segment table")
    sql_statements.append(f"-- Generated from {Path(csv_file_path).name}")
    sql_statements.append("")

    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        # Skip the header row
        next(csvfile, None)

        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 21:  # Need at least 21 columns for the data we need
                segment_code = row[0].strip()
                highway_number_str = row[1].strip()
                highway_letter = row[2].strip()
                direction = row[5].strip()
                length_str = row[8].strip()
                description = row[20].strip()

                # Skip empty rows
                if not segment_code or not highway_number_str:
                    continue

                try:
                    highway_number = int(highway_number_str)

                    # Generate hwy_code using same logic as highway script
                    if highway_letter:
                        # For entries with letters, use last 3 digits + letter (total 4 chars)
                        hwy_code = f"{highway_number:03d}{highway_letter}"
                    else:
                        # For entries without letters, use 4 digits
                        hwy_code = f"{highway_number:04d}"

                    # Parse length as float
                    length_km = float(length_str) if length_str else 0.0

                    # Validate direction (should be single character)
                    if len(direction) != 1:
                        print(f"Warning: Invalid direction '{direction}' for segment {segment_code}, skipping")
                        continue

                    # Escape single quotes in description
                    escaped_description = description.replace("'", "''")

                    # Generate UPSERT SQL statement
                    sql = f"""INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('{segment_code}', '{hwy_code}', '{escaped_description}', '{direction}', {length_km})
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";"""

                    sql_statements.append(sql)
                    sql_statements.append("")

                except (ValueError, IndexError) as e:
                    print(f"Warning: Skipping invalid row {row[:3]}...: {e}")
                    continue

    # Write to output file
    with open(output_sql_path, 'w', encoding='utf-8') as sqlfile:
        sqlfile.write('\n'.join(sql_statements))

    insert_count = len([s for s in sql_statements if s.startswith('INSERT')])
    print(f"Generated {insert_count} UPSERT statements")
    print(f"SQL file written to: {output_sql_path}")


def main():
    """Main function to run the script."""
    parser = argparse.ArgumentParser(
        description="Generate SQL UPSERT statements for the lki_segment table from a CSV file."
    )
    parser.add_argument(
        "csv_file",
        help="Path to the input CSV file containing segment data"
    )
    parser.add_argument(
        "-o", "--output",
        help="Path to the output SQL file (default: lki_segment_upsert.sql in the same directory as the script)",
        default=None
    )

    args = parser.parse_args()

    # Validate input CSV file exists
    csv_file_path = Path(args.csv_file)
    if not csv_file_path.exists():
        print(f"Error: CSV file not found at {csv_file_path}")
        sys.exit(1)

    # Determine output SQL file path
    if args.output:
        output_sql_path = Path(args.output)
    else:
        # Default: same directory as script with name based on input file
        script_dir = Path(__file__).parent
        input_filename = csv_file_path.stem  # Get filename without extension
        output_sql_path = script_dir / f"{input_filename}_upsert.sql"

    print(f"Input CSV: {csv_file_path}")
    print(f"Output SQL: {output_sql_path}")

    generate_upsert_sql(str(csv_file_path), str(output_sql_path))


if __name__ == "__main__":
    main()
