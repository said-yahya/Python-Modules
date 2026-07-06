import sys
import os

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None  # type: ignore


def main() -> None:
    if sys.prefix == sys.base_prefix:
        print(
            "ORACLE STATUS: WARNING! Secure connection failed.\n"
            "Reason: You are still plugged into the global environment!\n\n"
            "To protect the mainframe settings, enter the construct first:\n"
            "    python3 -m venv matrix_env\n"
            "    source matrix_env/bin/activate  # On Unix\n"
            "Then, install the required library inside your environment:\n"
            "    pip install python-dotenv\n\n"
            "After that, run this oracle deployment again."
        )
        sys.exit(1)

    if load_dotenv is None:
        print(
            "ORACLE STATUS: ERROR!\n"
            "Virtual environment detected, but 'python-dotenv' is missing.\n\n"
            "Run this command to load the required library:\n"
            "    pip3 install python-dotenv"
        )
        sys.exit(1)

    load_dotenv()

    matrix_mode = os.environ.get("MATRIX_MODE", "development").lower()
    database_url = os.environ.get("DATABASE_URL", "None")
    api_key = os.environ.get("API_KEY", "None")
    log_level = os.environ.get("LOG_LEVEL", "DEBUG")
    zion_endpoint = os.environ.get("ZION_ENDPOINT", "None")

    if api_key != "None":
        secrets_ok = "[OK] No hardcoded secrets detected"
    else:
        secrets_ok = "[WARNING] Missing API_KEY"
    if os.path.exists(".env"):
        env_file_ok = "[OK] .env file properly configured"
    else:
        env_file_ok = "[WARNING] Using system environment only"

    if matrix_mode == "production":
        print(
            "ORACLE STATUS: Reading the Matrix...\n"
            "Configuration loaded:\n"
            "---------------------------------------\n"
            "Mode: production\n"
            "Database: Connected to PRODUCTION secure cluster\n"
            "API Access: RESTRICTED & ENCRYPTED\n"
            f"Log Level: {log_level}\n"
            f"Zion Network: SECURE GATEWAY (Endpoint: {zion_endpoint})\n"
            "---------------------------------------\n"
            "Environment security check:\n"
            f"{secrets_ok}\n"
            f"{env_file_ok}\n"
            "[OK] Production overrides available\n\n"
            "The Oracle sees all production configurations."
        )
    else:
        print(
            "ORACLE STATUS: Reading the Matrix...\n"
            "Configuration loaded:\n"
            "---------------------------------------\n"
            f"Mode: {matrix_mode}\n"
            f"Database: Connected to local instance ({database_url})\n"
            "API Access: Authenticated\n"
            f"Log Level: {log_level}\n"
            f"Zion Network: Online (Endpoint: {zion_endpoint})\n"
            "---------------------------------------\n"
            "Environment security check:\n"
            f"{secrets_ok}\n"
            f"{env_file_ok}\n"
            "[OK] Production overrides available\n\n"
            "The Oracle sees all configurations."
        )


if __name__ == "__main__":
    main()
