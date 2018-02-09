#!/usr/bin/env python3 
#-*conding:utf-8-*-

# updated by XNiu2 on 09-Feb-2018
# https://www.codewars.com/kata/coloured-triangles/train/python



def puke(row):
    al = 'RGB'
    if row[0] == row[1]:
        return row[0]
    else:
        al = al.replace(row[0],'').replace(row[1], '')
    return al
    
def triangle(row):
    if (len(row) == 1):
        return row 
    ans = ''
    while True: 
        for i in range(0,len(row)-1):
            ans += puke(row[i:i+2])
        if (len(ans) == 1):
            break
        row = ans
        ans = ''
    return ans

print (triangle('R'))