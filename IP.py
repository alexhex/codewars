# ## IP Validation
import re
def is_valid_IP(strng):
    ip_lst = strng.split(".")
    if len(ip_lst) != 4:
        print 'Length Incorrect for %s' % strng
        # return False
    for ip_sec in ip_lst:
        print ip_sec
        if not re.match(r'^[0-9]\d+$', ip_sec):
            return False
        elif int(ip_sec) > 255 or int(ip_sec) < 0:
            # print 'IP section Fail for %s' % strn
            return False
    return True


# is_valid_IP('12.255.56.1')
# is_valid_IP('')
# is_valid_IP('abc.def.ghi.jkl')
# is_valid_IP('123.456.789.0')
# is_valid_IP('12.34.56')
# print is_valid_IP('12.34.56 .1')
# is_valid_IP('12.34.56.-1')
# is_valid_IP('123.045.067.089')
