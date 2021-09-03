"""Main executable routine."""
import argparse


def parse_args() -> argparse.Namespace:
    """Parse command line arguments.

    :return: parsed command line arguments
    """
    parser = argparse.ArgumentParser()
    return parser.parse_args()


def main() -> None:
    """Main script routine."""
    args = parse_args()
    print(args)


if __name__ == "__main__":
    main()
