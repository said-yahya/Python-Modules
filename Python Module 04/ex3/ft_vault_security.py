def secure_archive(f, mode='r', ctn="") -> tuple[bool, str]:
    try:
        if mode == 'r':
            with open(f, 'r') as f:
                data = f.read()
            return (True, data)
        elif mode == 'w':
            with open(f, 'w') as f:
                f.write(ctn)
            return (True, f"Content successfully written to {(f.name)}")
        else:
            return (False, f"Invalid mode: {mode}. Use 'r' or 'w'.")

    except Exception as e:
        return (False, str(e))


if __name__ == "__main__":
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(f"{secure_archive("nonexistent_file.txt", "r")}\n")

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(f"{secure_archive("/etc/master.passwd", "r")}\n")

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(f"{secure_archive("example", "r")}\n")
    status, content = secure_archive("example", "r")

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(f"{secure_archive("new", "w", content)}\n")
