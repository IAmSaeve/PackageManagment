#!/usr/bin/python

import os
import sys
import time
import random
import concurrent.futures
import urllib.request
import json

maxThreads = 4

def task():
    rnd = random.randint(0, 99999999999) + random.random()
    print(f"PID: {os.getpid()}, with number {rnd}")
    try:
        jsonData = json.dumps({"num": rnd})
        jsonBytes = jsonData.encode('utf-8')
        req = urllib.request.Request("http://localhost:7000/echo")
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        urllib.request.urlopen(req, jsonBytes)
    except Exception:
        print("Error sending data!")
        return
    finally:
        time.sleep(1)


def main_loop():
    with concurrent.futures.ProcessPoolExecutor(max_workers=maxThreads) as executor:
        for _ in range(0, maxThreads):
            executor.submit(task)


if __name__ == "__main__":
    try:
        while 1:
            main_loop()
    except KeyboardInterrupt:
        print("\nExiting by user request.\n")
        sys.exit(0)

