def camel_case(a_string):
    if a_string == '':
        return ''
    stripped = a_string.split(' ')
    c_cased = []
    for i in stripped:
        temp = i[0].upper() + i[1:]
        c_cased.append(temp)
    return ' '.join(c_cased)
