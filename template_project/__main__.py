import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    return parser.parse_args()


def main() -> None:
    args = parse_args()
