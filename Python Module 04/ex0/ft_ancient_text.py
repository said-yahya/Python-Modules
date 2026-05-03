from typing import IO
import sys


def main() -> None:
    input = sys.argv
    if len(input) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{input[1]}'")
        try:
            content: IO = open(input[1], 'r')
            print("---\n")
            print(content.read())
            print("\n---")
            content.close()
            print(f"File '{input[1]}' closed.")
        except Exception as e:
            print(f"Error: {e}\n")
            return


if __name__ == "__main__":
    main()
