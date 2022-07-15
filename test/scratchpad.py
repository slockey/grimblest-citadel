
from dataclasses import dataclass
from tkinter import N


def main() -> None:

    alien = {'color': 'green', 'points': 5}

    # access the dataclass
    print(alien['color'])
    print(alien['points'])

if __name__ == "__main__":
    main()
