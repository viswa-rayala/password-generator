# Password Generator

A small command-line password generator written in Python. The script creates a password using uppercase and lowercase letters, numbers, and punctuation characters.

## Requirements

- Python 3

No external packages are required.

## Usage

Run the script from the project directory:

```bash
python3 password_generator.py
```

When prompted, enter the desired password length:

```text
enter the length of the password: 12
```

The generated password is then printed to the terminal:

```text
gT7!qP2@xL9$
```

## How It Works

The generator builds a character pool from:

- Uppercase and lowercase letters
- Digits from `0` to `9`
- Python punctuation characters

It selects one random character from this pool for each position in the requested password length.

## Project Structure

```text
.
├── password_generator.py
└── README.md
```

## Note

This project uses Python's `random` module for simple password generation. For passwords intended to protect real accounts or sensitive data, use a cryptographically secure generator such as Python's `secrets` module or a trusted password manager.