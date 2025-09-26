#!/usr/bin/env python3
"""
Script to generate SQL UPSERT statements for the lki_highway table
from a CSV file.
"""

import csv
import os
import sys
import argparse
from pathlib import Path


def generate_upsert_sql(csv_file_path: str, output_sql_path: str) -> None:
    """
    Generate UPSERT SQL statements for the lki_highway table from CSV data.

    Args:
        csv_file_path: Path to the input CSV file
        output_sql_path: Path to write the output SQL file
    """
    if not os.path.exists(csv_file_path):
        print(f"Error: CSV file not found at {csv_file_path}")
        sys.exit(1)

    sql_statements = []
    sql_statements.append("-- UPSERT statements for lki_highway table")
    sql_statements.append(f"-- Generated from {Path(csv_file_path).name}")
    sql_statements.append("")

    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        # Skip the header row
        next(csvfile, None)

        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 3:
                number_str, letter, description = row[0], row[1], row[2]

                # Skip empty rows
                if not number_str.strip():
                    continue

                try:
                    number = int(number_str.strip())

                    # Clean up the letter (remove extra spaces)
                    letter = letter.strip() if letter.strip() else ''

                    # Clean up description
                    description = description.strip()

                    # Generate code as 4-digit zero-padded number + letter, but ensure total is 4 chars
                    if letter:
                        # For entries with letters, use last 3 digits + letter (total 4 chars)
                        code = f"{number:03d}{letter}"
                    else:
                        # For entries without letters, use 4 digits
                        code = f"{number:04d}"

                    # Escape single quotes in description
                    escaped_description = description.replace("'", "''")

                    # Generate UPSERT SQL statement
                    sql = f"""INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('{code}', {number}, '{letter}', '{escaped_description}')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";"""

                    sql_statements.append(sql)
                    sql_statements.append("")

                except ValueError as e:
                    print(f"Warning: Skipping invalid row {row}: {e}")
                    continue

    # Write to output file
    with open(output_sql_path, 'w', encoding='utf-8') as sqlfile:
        sqlfile.write('\n'.join(sql_statements))

    print(f"Generated {len([s for s in sql_statements if s.startswith('INSERT')])} UPSERT statements")
    print(f"SQL file written to: {output_sql_path}")


def main():
    """Main function to run the script."""
    parser = argparse.ArgumentParser(
        description="Generate SQL UPSERT statements for the lki_highway table from a CSV file."
    )
    parser.add_argument(
        "csv_file",
        help="Path to the input CSV file containing highway data"
    )
    parser.add_argument(
        "-o", "--output",
        help="Path to the output SQL file (default: lki_highway_upsert.sql in the same directory as the script)",
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
