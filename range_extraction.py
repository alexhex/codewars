#!/usr/bin/python3
#-*-coding:utf-8-*-

def solutions(args):
    prev = args.pop(0)
    last = None
    answer = "%s" % prev
    for item in args:
        if item == prev + 1:
            last = item
        else:
            if last is None:
                answer += ", %s" % item
            else:
                answer += "-%s, %s" % (last, item)
        prev = item
    return answer

print (solutions([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))

            