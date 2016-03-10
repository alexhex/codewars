def lcs(x, y):
    lst_x, lst_y = [], []
    common_str_prefix, common_str_suffix = [], []

    for letter in x:
        if letter in y:
            lst_x.append(letter)

    for letter in y:
        if letter in x:
            lst_y.append(letter)

    while lst_x[0] == lst_y[0]:
        common_str_prefix.append(lst_x[0])
        del lst_x[0]
        del lst_y[0]

    while lst_x[-1] == lst_y[-1]:
        common_str_suffix.append(lst_x[-1])
        del lst_x[-1]
        del lst_y[-1]

    print lst_x, lst_y,common_str_prefix

lcs( "132535365" , "123456789" )
#lcs( "" , "" )
