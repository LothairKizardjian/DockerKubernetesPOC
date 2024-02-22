#!/bin/bash
import logging
import random
import time

while True:
    time.sleep(1)
    logging.warning(f"ID : {random.randint(0, 100)} - Hello World !")
