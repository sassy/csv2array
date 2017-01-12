#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv

def csv2array(filename):
    f = open(filename, 'r')
    output = open('output.txt', 'w')
    reader = csv.reader(f)
    header = next(reader)

    output.write("[\n")
    for row in reader:
        output.write("{\n")
        output.write("    " + header[0] + ": ")
        output.write(row[0].strip() + ",\n")
        output.write("    " + header[1] + ": ")
        output.write("\"" + row[1].strip() + "\"\n")
        output.write("},\n")

    output.write("]\n")
    output.close()
    f.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        csv2array(sys.argv[1])
