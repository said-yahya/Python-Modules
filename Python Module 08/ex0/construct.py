import sys
import os
import site


if __name__ == "__main__":
    if sys.prefix != sys.base_prefix:
        print("MATRIX STATUS: Welcome to the construct\n\n"
              f"Current Python: {sys.executable}\n"
              f"Virtual Environments: {os.path.basename(sys.prefix)}\n"
              f"Environment Path: {sys.prefix}\n\n"
              "SUCCESS: You're in an isolated environment!\n"
              "Safe to install packages without affecting the global system."
              f"\n\nPackage installation path: {site.getsitepackages()[0]}")
    else:
        print("MATRIX STATUS: You're still plugged in\n\n"
              f"Current Python: {sys.executable}\n"
              "Virtual Environment: None detected\n\n"
              "WARNING: You're in the global environment!\n"
              "The machines can see everything you install.\n\n"
              "To enter the construct, run:\n"
              "python3 -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              "matrix_env\\Scripts\\activate # On Windows\n\n"
              "Then run this program again.")
