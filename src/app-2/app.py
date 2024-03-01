#!/bin/bash
import random
import time

from filelock import FileLock

id = random.randint(0, 100)
filename = "/python-app/test-file.txt"
lock = FileLock(filename + ".lock")

while True:
    time.sleep(1)
    with lock:
        with open(filename, "a+") as test_file:
            test_file.write(f"App 2 : Hello World !\n")
