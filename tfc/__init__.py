from argparse import ArgumentParser

from .tfc import Translation


def main():
    parser = ArgumentParser(description="Simple Translate App From The Clipboard")
    parser.add_argument("--dest", help="destination language", default="tr")
    parser.add_argument("--src", help="source language", default="auto")
    options = parser.parse_args()

    print("TFC listens To Your Clipboard For Translation.")
    print("="*50)

    translation = Translation(options.dest, options.src)
    translation.start()


if __name__ == "__main__":
    main()
