#!/usr/bin/python3
#-*-coding:utf-8-*-


def solution(a):
    tag = 1 
    b = []
    while (tag):
        tag = 0
        a.sort()
        min_val = a[0]
        b = []
        for item in a:
            if item != min_val:
                tag = 1
                if item % min_val != 0:
                    item = item % min_val
                else:
                    item = min_val
            b.append(item)
        if tag:
            a = b
    
    return sum(b)

print (solution([9]))