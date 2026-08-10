def process_scores(scores: dict[str, int]) -> None:
    for name, score in scores.items():
        print(f"{name}: {score}")


scores: dict[str, int] = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 95,
}

process_scores(scores)