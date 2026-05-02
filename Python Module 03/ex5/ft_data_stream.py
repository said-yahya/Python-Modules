from typing import Generator
import random


def gen_event() -> Generator[tuple, None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
                "move", "eat", "sleep", "grab", "run",
                "climb", "swim", "use", "release"
                ]
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(event_list: list) -> Generator[tuple, None, None]:
    while len(event_list) > 0:
        idx = random.randrange(len(event_list))
        event = event_list.pop(idx)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event_gen = gen_event()

    for i in range(1000):
        player, action = next(event_gen)
        print(f"Event {i}: Player {player} did action {action}")

    ten_events: list[tuple[str, str]] = []
    for _ in range(10):
        ten_events += [next(event_gen)]
    print(f"\nBuilt list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
