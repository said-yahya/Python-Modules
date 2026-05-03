import typing
import sys


def main() -> None:
    args = sys.argv
    if len(args) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{args[1]}'")
        try:
            f: typing.IO = open(args[1], 'r')
            content: str = f.read()
            print("---\n")
            print(content)
            print("\n---")
            f.close()
            print(f"File '{args[1]}' closed.")
            transformed_content: str = content.replace('\n', '#\n')
            if not transformed_content.endswith('#\n'):
                transformed_content += "#"
            print("Transform data:")
            print("---\n")
            print(transformed_content)
            print("\n---")
            file: str = input("Enter new file name (or empty):")
            if file:
                new_file: typing.IO = open(file, 'w')
                new_file.write(transformed_content)
                new_file.close()
                print(f"Saving data to '{file}'")
                print(f"Data saved in file '{file}'")
            else:
                print("Not saving data.")
        except Exception as e:
            print(f"Error: {e}\n")
            return


if __name__ == "__main__":
    main()
