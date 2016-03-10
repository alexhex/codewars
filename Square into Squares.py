# Square into Squares. Protect trees!

# This function is to judge if the given num is a Perfect Square Expression
def is_pse(num):
    i = 1
    while num > 0:
        num -= 2 * i - 1
        i += 1
    return num == 0

def decompose(n):
    # your code
    fac = []
    for i in range(1,n):
        fac.append(i ** 2)
    print fac

    sqr = n ** 2
    ans = []
    while len(fac) > 0:
        for i in range(len(fac)-1, -1, -1):
            if sqr > fac[i]:
                sqr -= fac[i]
                ans.append(i+1)
        if sqr == 0:
            return ans
        else:
            fac.pop()
            print 'fac is now', fac




decompose(10)
