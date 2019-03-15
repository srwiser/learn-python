#!/usr/bin/env python
import sys

def findHotel():
    loopcounter = int(input())
    avgs = []
    for i in range(loopcounter):
        id_avg = tuple(int(x.strip()) for x in input().split(' '))
        # id, avg = [int(x) for x in input().split()]
        # id, avg = map(int, input().split())
        # avgs.update({id: avg})
        avgs.append(id_avg)
        # revDct = dict((id, avg) for (id, avg) in avgs)
    print("Value : %s" % avgs)
    # print("Value : %s" % revDct)

if __name__ == '__main__':
    findHotel()
