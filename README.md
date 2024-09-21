# Apple Passwords to Bitwarden Converter

## Overview

This project provides a simple Python script to convert Apple Passwords exports to a format compatible with Bitwarden password manager. It takes a CSV file exported from Apple Passwords and transforms it into a CSV file that can be imported into Bitwarden.

## Features

- Converts Apple Passwords CSV export to Bitwarden-compatible CSV format
- Handles common fields such as name, URL, username, password, notes, and TOTP
- Utilizes pandas for efficient CSV processing
- Command-line interface for easy usage

## Requirements

- Python 3.12 or higher
- pandas library

## Setup

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/apple-password-to-bitwarden.git
   cd apple-passwords-to-bitwarden
   ```

2. Install dependencies using Poetry:

   ```
   poetry install
   ```

   If you don't have Poetry installed, you can install it following the instructions at https://python-poetry.org/docs/#installation

   Alternatively, you can use pip to install the required packages:

   ```
   pip install pandas
   ```

## Usage

1. Export your passwords from Apple Passwords to a CSV file.

2. Run the script with the path to your exported CSV file:

   ```
   python main.py path/to/your/passwords.csv
   ```

3. The script will generate a new file named `bitwarden-passwords.csv` in the same directory as the script.

4. Import the generated `bitwarden-passwords.csv` file into Bitwarden.
