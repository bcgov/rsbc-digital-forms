# LKI Highway SQL Generator

A Python script that generates PostgreSQL UPSERT statements for the `lki_highway` table from CSV data.

## Overview

This script reads highway data from a CSV file and generates SQL INSERT statements with ON CONFLICT clauses (UPSERT) to populate or update the `TAR.lki_highway` table. The script ensures data integrity by properly formatting codes and escaping special characters.

## Features

- **Flexible Input**: Accepts any CSV file path as a command-line argument
- **Code Formatting**: Generates exactly 4-character codes (3 digits + letter for entries with letters, 4 digits for entries without)
- **SQL Escaping**: Properly handles special characters in descriptions (e.g., single quotes)
- **Error Handling**: Validates input files and provides clear error messages
- **PostgreSQL Compatible**: Uses `INSERT ... ON CONFLICT ... DO UPDATE` syntax

## Prerequisites

- Python 3.6+
- CSV file with highway data in the expected format

## Installation

No installation required. The script uses only Python standard library modules.

## Usage

### Basic Usage

```bash
python3 generate_lki_hwy_sql_scripts.py /path/to/highway-data.csv
```

### With Custom Output Path

```bash
python3 generate_lki_hwy_sql_scripts.py /path/to/highway-data.csv -o custom_output.sql
```

### Help

```bash
python3 generate_lki_hwy_sql_scripts.py --help
```

## Command-Line Arguments

- `csv_file` (required): Path to the input CSV file containing highway data
- `-o, --output` (optional): Path to the output SQL file. If not specified, defaults to `{input_filename}_upsert.sql` in the same directory as the script

## Input CSV Format

The CSV file must contain at least 3 columns in this order:

| Column | Description | Example |
|--------|-------------|---------|
| Number | Highway number (integer) | `1`, `97`, `395` |
| Letter | Highway letter suffix (optional) | `A`, `B`, `C` (can be empty) |
| Description | Highway description | `TRANS-CANADA`, `OKANAGAN - CARIBOO - ALASKA` |

### Example CSV Content

```csv
Number,Letter,Description
1,,TRANS-CANADA
1,A,REPLACED TRANS-CANADA SECTIONS
97,,OKANAGAN - CARIBOO - ALASKA
97,C,OKANAGAN CONNECTOR - LOGAN LAKE - CACHE CREEK
395,,CHRISTINA LAKE - LAURIER
```

## Output Format

The script generates PostgreSQL UPSERT statements for the `TAR.lki_highway` table:

### Code Generation Rules

- **Highways without letters**: 4-digit zero-padded number (e.g., `0001`, `0097`, `0395`)
- **Highways with letters**: 3-digit zero-padded number + letter (e.g., `001A`, `097C`)

### Example Output

```sql
-- UPSERT statements for lki_highway table
-- Generated from highway-data.csv

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0001', 1, '', 'TRANS-CANADA')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('001A', 1, 'A', 'REPLACED TRANS-CANADA SECTIONS')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";
```

## Database Schema

The generated SQL is designed for this table structure:

```sql
CREATE TABLE "TAR"."lki_highway" (
    "code" VARCHAR(4) PRIMARY KEY,
    "number" INTEGER NOT NULL,
    "letter" VARCHAR(1),
    "description" VARCHAR(100) NOT NULL
);
```

## Error Handling

The script includes robust error handling:

- **File Not Found**: Exits with error if the input CSV file doesn't exist
- **Invalid Data**: Skips rows with invalid highway numbers and shows warnings
- **Empty Rows**: Automatically skips empty rows
- **SQL Injection Protection**: Escapes single quotes in descriptions

## Examples

### Example 1: Basic Usage

```bash
$ python3 generate_lki_hwy_sql_scripts.py highway-data.csv
Input CSV: highway-data.csv
Output SQL: highway-data_upsert.sql
Generated 79 UPSERT statements
SQL file written to: highway-data_upsert.sql
```

### Example 2: Custom Output Path

```bash
$ python3 generate_lki_hwy_sql_scripts.py /data/highway-data.csv -o /sql/insert_highways.sql
Input CSV: /data/highway-data.csv
Output SQL: /sql/insert_highways.sql
Generated 79 UPSERT statements
SQL file written to: /sql/insert_highways.sql
```

### Example 3: Error Case

```bash
$ python3 generate_lki_hwy_sql_scripts.py nonexistent.csv
Error: CSV file not found at nonexistent.csv
```

## Troubleshooting

### Common Issues

1. **"CSV file not found"**: Ensure the file path is correct and the file exists
2. **"Unknown format code 'd'"**: This indicates invalid data in the Number column (must be integers)
3. **Empty output file**: Check that your CSV has the correct column structure and contains valid data

### CSV Format Tips

- Ensure the first row contains headers (they will be skipped)
- Highway numbers must be valid integers
- Letter column can be empty (just leave it blank)
- Descriptions can contain special characters (they will be properly escaped)

## License

This script is part of the rsbc-digital-forms project.
