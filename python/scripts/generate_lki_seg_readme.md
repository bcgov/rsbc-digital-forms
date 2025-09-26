# LKI Segment SQL Generator

A Python script that generates PostgreSQL UPSERT statements for the `lki_segment` table from CSV data.

## Overview

This script reads segment data from a CSV file and generates SQL INSERT statements with ON CONFLICT clauses (UPSERT) to populate or update the `TAR.lki_segment` table. The script ensures data integrity by properly formatting codes, validating directions, and escaping special characters.

## Features

- **Flexible Input**: Accepts any CSV file path as a command-line argument
- **Code Formatting**: Uses existing 4-character segment codes and generates highway codes (3 digits + letter for entries with letters, 4 digits for entries without)
- **Data Validation**: Validates direction fields (must be single character) and numeric fields
- **SQL Escaping**: Properly handles special characters in descriptions (e.g., single quotes)
- **Error Handling**: Validates input files and provides clear error messages
- **PostgreSQL Compatible**: Uses `INSERT ... ON CONFLICT ... DO UPDATE` syntax

## Prerequisites

- Python 3.6+
- CSV file with segment data in the expected format

## Installation

No installation required. The script uses only Python standard library modules.

## Usage

### Basic Usage

```bash
python3 generate_lki_seg_sql_scripts.py /path/to/segment-data.csv
```

### With Custom Output Path

```bash
python3 generate_lki_seg_sql_scripts.py /path/to/segment-data.csv -o custom_output.sql
```

### Help

```bash
python3 generate_lki_seg_sql_scripts.py --help
```

## Command-Line Arguments

- `csv_file` (required): Path to the input CSV file containing segment data
- `-o, --output` (optional): Path to the output SQL file. If not specified, defaults to `{input_filename}_upsert.sql` in the same directory as the script

## Input CSV Format

The CSV file must contain at least 21 columns. The script uses these specific columns:

| Column Index | Column Name | Description | Example |
|--------------|-------------|-------------|---------|
| 0 | Segment | 4-character segment code | `0203`, `0356`, `5007` |
| 1 | Highway_Number | Highway number (integer) | `1`, `97`, `916` |
| 2 | Highway_Letter | Highway letter suffix (optional) | `A`, `B`, `C` (can be empty) |
| 5 | Direction | Direction (single character) | `N`, `S`, `E`, `W` |
| 8 | Length | Segment length in kilometers (float) | `0.30`, `9.97`, `25.76` |
| 20 | Description | Segment description | `NB EXIT FROM GOLDEN EARS - 113B AVE` |

### Example CSV Content

```csv
Segment,Highway_Number,Highway_Letter,Hwy2,Hwy3,Direction,Search_Sequence,Report_Sequence,Length,Revision_Date,Effective_Date,Create_Date,Road_Add_Date,Devolved_Date,Begin_Node,Begin_Continuity,End_Node,End_Continuity,Nway,Opposite_Segment,Description,Hwy_Km_Begin,Hwy_Km_End,Hwy_Km_Year
0203,916,,,,N,5,6,0.30,7/15/18,3/1/11,7/1/10,7/1/10,,NULL0203,D,0207NULL,D,1,,NB EXIT FROM GOLDEN EARS - 113B AVE,,,
0356,19,A,,,N,1,1,0.99,7/15/19,1/1/00,4/1/95,4/1/95,,04670356,C,03562317,C,2,,BRECHIN RD: STEWART AVE (DEPT.BAY) - ISLAND HWY,,,
5007,19,,,,S,24,4,18.88,7/19/23,1/1/24,7/19/23,1/1/00,,50062318,C,5007NULL,D,1,5006,NANAIMO PARKWAY SOUTHBOUND,140.916,159.757,2021
```

## Output Format

The script generates PostgreSQL UPSERT statements for the `TAR.lki_segment` table:

### Code Generation Rules

- **Segment Code**: Uses the existing 4-character code from the "Segment" column directly
- **Highway Code**: Generated from Highway_Number and Highway_Letter:
  - Highways without letters: 4-digit zero-padded number (e.g., `0916`, `0001`)
  - Highways with letters: 3-digit zero-padded number + letter (e.g., `019A`, `097C`)

### Example Output

```sql
-- UPSERT statements for lki_segment table
-- Generated from SEGMENT-Table 1.csv

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0203', '0916', 'NB EXIT FROM GOLDEN EARS - 113B AVE', 'N', 0.3)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0356', '019A', 'BRECHIN RD: STEWART AVE (DEPT.BAY) - ISLAND HWY', 'N', 0.99)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";
```

## Database Schema

The generated SQL is designed for this table structure:

```sql
CREATE TABLE "TAR"."lki_segment" (
    "code" VARCHAR(4) PRIMARY KEY,
    "hwy_code" VARCHAR(4) NOT NULL REFERENCES "TAR"."lki_highway"("code"),
    "description" VARCHAR(100) NOT NULL,
    "direction" VARCHAR(1) NOT NULL,
    "length_km" FLOAT NOT NULL
);
```

## Error Handling

The script includes robust error handling:

- **File Not Found**: Exits with error if the input CSV file doesn't exist
- **Invalid Data**: Skips rows with invalid highway numbers, directions, or lengths and shows warnings
- **Empty Rows**: Automatically skips empty rows
- **Direction Validation**: Ensures direction is exactly one character (N, S, E, W)
- **SQL Injection Protection**: Escapes single quotes in descriptions

## Examples

### Example 1: Basic Usage

```bash
$ python3 generate_lki_seg_sql_scripts.py SEGMENT-Table\ 1.csv
Input CSV: SEGMENT-Table 1.csv
Output SQL: SEGMENT-Table 1_upsert.sql
Generated 446 UPSERT statements
SQL file written to: SEGMENT-Table 1_upsert.sql
```

### Example 2: Custom Output Path

```bash
$ python3 generate_lki_seg_sql_scripts.py /data/segment-data.csv -o /sql/insert_segments.sql
Input CSV: /data/segment-data.csv
Output SQL: /sql/insert_segments.sql
Generated 446 UPSERT statements
SQL file written to: /sql/insert_segments.sql
```

### Example 3: Error Case

```bash
$ python3 generate_lki_seg_sql_scripts.py nonexistent.csv
Error: CSV file not found at nonexistent.csv
```

## Troubleshooting

### Common Issues

1. **"CSV file not found"**: Ensure the file path is correct and the file exists
2. **"Unknown format code 'd'"**: This indicates invalid data in the Highway_Number column (must be integers)
3. **"Invalid direction"**: Direction must be exactly one character (N, S, E, W)
4. **Empty output file**: Check that your CSV has at least 21 columns and contains valid data

### CSV Format Tips

- Ensure the first row contains headers (they will be skipped)
- Segment codes should be exactly 4 characters
- Highway numbers must be valid integers
- Direction must be a single character (N, S, E, W)
- Length values should be valid decimal numbers
- Descriptions can contain special characters (they will be properly escaped)

## Dependencies

The `lki_segment` table has a foreign key relationship with `lki_highway`. Ensure that the corresponding highway records exist in the `TAR.lki_highway` table before running the generated SQL.

## License

This script is part of the rsbc-digital-forms project.</content>
<parameter name="filePath">/Users/adimarborges/dev/rsbc-digital-forms/python/scripts/generate_lki_seg_readme.md
