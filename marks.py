'''
Program to Merge two csv files into one in a smart way
'''

import csv
import os
from sys import argv
from os.path import exists
import settings_local


def csvtodict(file):
    reader = csv.reader(open(file,'rb'))
    result = {}
    header = next(reader)
    for row in reader:
        key = row[0]
        result[key] = row[1] if row[1] != "" else 'NA'  ##Conditional Assignment
    return header, result

# def mergedict(d1,d2):
#     ds = [d1, d2]
#     d = {}
#     for key in d1.iterkeys():
#         d[key] = tuple(d[key] for d in ds)
#     return d

def dicttocsv(header1, header2, result1, result2, outputfile):
    with open(outputfile, 'wb') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([header1[0].strip(), header1[1].strip(),header2[1].strip()])
        for key in result1:
            writer.writerow([key, result1[key], result2[key]])

def main():
    try:
        script, file1, file2, file3 = argv
        base_folder = os.path.abspath(os.path.dirname(__file__))
        folder = settings_local.files['foldername']
        full_path = os.path.join(base_folder, folder)

        f1 = (full_path + '/' + file1)
        f2 = (full_path + '/' + file2)
        outputfile = (full_path + '/' + file3)

        header1, result1 = csvtodict(f1)
        header2, result2 = csvtodict(f2)
        dicttocsv(header1, header2, result1, result2, outputfile)
        print "Successfully written to " + outputfile
    except:
        print "Usage: python marks.py file1.csv file2.csv output.csv"


if __name__ == '__main__':
    main()