import sys

import pandas as pd


def main(input_file: str):
    apple_passwords_df = pd.read_csv(input_file)
    bitwarden_df = apple_passwords_df.rename(
        columns={
            "Title": "name",
            "URL": "login_uri",
            "Username": "login_username",
            "Password": "login_password",
            "Notes": "notes",
            "OTPAuth": "login_totp",
        }
    )
    bitwarden_df.to_csv("bitwarden-passwords.csv", index=False)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
