import pandas as pd


def main():
    apple_passwords_df = pd.read_csv("Passwords.csv")

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
    main()
