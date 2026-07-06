import sys
import importlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

REQUIRED_PACKAGES = ["pandas", "numpy", "matplotlib"]


def check_dependencies() -> dict[str, str | None]:
    status = {}
    for package in REQUIRED_PACKAGES:
        try:
            module = importlib.import_module(package)
            status[package] = getattr(module, "__version__", "unknown")
        except ImportError:
            status[package] = None
    return status


def print_missing_instructions() -> None:
    print(
        "ERROR: Missing dependencies to enter the Matrix!\n\n"
        "To install via pip (Classic approach):\n"
        "    pip install -r requirements.txt\n"
        "    python3 loading.py\n\n"
        "To install via Poetry (Modern approach):\n"
        "    poetry install\n"
        "    poetry run python loading.py"
    )


def run_analysis() -> None:

    print(
        "Analyzing Matrix data...\n"
        "Processing 1000 data points...\n"
        "Generating visualization..."
    )

    matrix_signals = np.random.randn(1000)
    df = pd.DataFrame(matrix_signals, columns=["Signal Intensity"])

    plt.figure(figsize=(16, 9))
    plt.plot(df["Signal Intensity"], color="green", alpha=0.7)
    plt.title("Matrix Data Stream Analysis", fontsize=14, color="green")
    plt.xlabel("Data Points", fontsize=12)
    plt.ylabel("Intensity", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.5)

    output_file = "matrix_analysis.png"
    plt.savefig(output_file)
    plt.close()

    print(
        f"\nAnalysis complete!\n"
        f"Results saved to: {output_file}"
    )


def main() -> None:
    if sys.prefix == sys.base_prefix:
        print(
            "LOADING STATUS: WARNING! Environment is unsafe.\n"
            "Reason: You are attempting to run this in the global ecosystem!"
            "\n\nTo prevent cluttering your OS, enter the virtual environment"
            " first:\n    python3 -m venv matrix_env\n"
            "    source matrix_env/bin/activate  # On Unix/Mac\n"
            "    matrix_env\\Scripts\\activate     # On Windows\n\n"
            "Once inside, install dependencies and run the program safely."
        )
        sys.exit(1)

    print(
        "LOADING STATUS: Loading programs...\n"
        "Checking dependencies:"
    )

    pkg_status = check_dependencies()

    all_ok = True
    for pkg, version in pkg_status.items():
        if version:
            print(f"[OK] {pkg} ({version})")
        else:
            print(f"[MISSING] {pkg}")
            all_ok = False

    print("---------------------------------------")

    if not all_ok:
        print_missing_instructions()
        sys.exit(1)

    print(
        "Data manipulation ready\n"
        "Numerical computation ready\n"
        "Visualization ready\n"
    )
    run_analysis()


if __name__ == "__main__":
    main()
