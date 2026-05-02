import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    l: list[int] = []
    i: int = 1
    while (i < len(sys.argv)):
        try:
            num: int = int(sys.argv[i])
            l += [num]
        except ValueError:
            print(f"Invalid parameter: {sys.argv[i]}")
        i += 1
    if len(l) == 0:
        print(
                "No scores provided. Usage: python3 ft_score_analytics.py "
                "<score1> <score2> ..."
            )
    else:
        print(f"Scores processed: {l}")
        print(f"Total payers: {len(l)}")
        print(f"Average score: {sum(l) / len(l)}")
        print(f"High score: {max(l)}")
        print(f"Low score: {min(l)}")
        print(f"Score range: {max(l) - min(l)}")


if __name__ == "__main__":
    main()
