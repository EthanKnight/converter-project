#!/usr/bin/python3

'''
    converter.py
    This program inputs a Base10 number, and outputs the correspoding:
        Binary (Base2), Hex (Base16), and Ascii character
    Creator:   Ethan Knight
    Email:     ethantknight@gmail.com
    Published: 20181116
'''

import sys
import time

def main():
    print("\n", sys.version_info)
    try:
        while True:
            print("\n\nPress Ctrl+C to exit.")
            while True:
                try:
                    num=int(input("Enter an integer to convert\n\n\t"))
                    break
                except ValueError:
                    print("\nThat's not an integer.")
            output(abs(num))
            time.sleep(.5)
    except KeyboardInterrupt:
        print("\tProgram Terminated\n\n")
        sys.exit(0)

def output(num):
    bnum = bin(num)[2:]
    hnum = hex(num)[2:]
    print("\nBinary:\t",    bnum)
    print("Hex:\t",         hnum)
    hnum = join(hnum)
    print("Ascii:\t", bytearray.fromhex(hnum).decode(encoding="Latin1"))

def join(hnum):
    seq = ("0", hnum)
    if (len(hnum)%2!=0):
        hnum="".join(seq)
    return hnum

if __name__=="__main__":
    main()
