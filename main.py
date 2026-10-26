import os

import util
from tasks import task1, task2, task3, task4, task5, task6


def main():
    os.makedirs(util.OUT_DIR, exist_ok=True)

    task1.run()
    task2.run()
    task3.run()
    task4.run()
    task5.run()
    task6.run()


if __name__ == "__main__":
    main()
