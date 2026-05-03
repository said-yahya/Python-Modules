import sys
import typing


def main() -> None:
    args = sys.argv
    if len(args) != 2:
        sys.stderr.write("Usage: ft_stream_management.py <file>\n")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{args[1]}'")

    try:
        f: typing.IO = open(args[1], 'r')
        content: str = f.read()
        f.close()

        print("---\n" + content + "\n---")
        print(f"File '{args[1]}' closed.")

        transformed_content: str = content.replace('\n', '#\n')
        if not transformed_content.endswith('#\n'):
            transformed_content += "#"

        print("Transform data:\n---")
        print(transformed_content + "\n---")
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        new_filename = sys.stdin.readline().strip()

        if new_filename:
            print(f"Saving data to '{new_filename}'")
            try:
                new_file: typing.IO = open(new_filename, 'w')
                new_file.write(transformed_content)
                new_file.close()
                print(f"Data saved in file '{new_filename}'")
            except Exception as e:
                sys.stderr.write(
                                    "[STDERR] Error opening file "
                                    f"'{new_filename}': {e}\n")
                print("Data not saved.")
        else:
            print("Not saving data.")

    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{args[1]}': {e}\n")
        return


if __name__ == "__main__":
    main()
