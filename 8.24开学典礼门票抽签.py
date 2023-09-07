#!/usr/bin/env python3

import requests
import numpy as np
import argparse

def main():
    total = 39
    selected = [9, 3]

    latest_hash = requests.get('https://blockchain.info/latestblock').json()['hash']
    np.random.seed(int(latest_hash[-8:], 16))  # since the seed should be less than 2**32
    print(latest_hash[-8:])

    ticket_type = 0
    for s in selected:
        people_permutation = np.random.permutation(total)
        ticket_type += 1
        selected = people_permutation[:s]
        for p in sorted(selected):
            print(f'{p+2} is selected for ticket type {ticket_type}.')


if __name__ == '__main__':
    main()