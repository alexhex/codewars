#!usr//bin//python3
#-*-coding:utf-8-*-

#[XNiu2 2018-02-07]

# def palindrome(n, c):
#     h = n//2
#     if h != 0:
#         if n % 2 == 0:
#             new_c = (h//len(c))*c + c[0:(h%len(c))]
#             ans = new_c + new_c[::-1]
#         else:
#             new_c = c[0:(len(c)-1)]
#             half_len = len(new_c)
#             new_c = (h//half_len)*new_c + new_c[h%half_len]
#             ans = new_c + c[-1] + new_c[::-1]
#     else:
#         return c
#     return ans

def palindrome(n, c):
    h = n//2
    new_c = (h//len(c)) * c + c[0:(h%len(c))]
    return (new_c+new_c[::-1]) if (n%2 == 0) else (new_c+c[-1]+new_c[::-1])
print (palindrome(1, "a"))