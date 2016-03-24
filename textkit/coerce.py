
def isfloat(value):
    try:
        float(value)
        return True
    except:
        return False


def isint(value):
    try:
        int(value)
        return True
    except:
        return False


def coerce_types(content):
    if len(content) == 0:
        return content
    col_count = len(content[0])
    # first test data types
    test_count = 2
    converters = []
    for r_ind in range(test_count):
        for col in content[r_ind]:
            # test
            if(isint(col)):
                converters.append(lambda x: int(x))
            elif(isfloat(col)):
                converters.append(lambda x: float(x))
            else:
                converters.append(lambda x: x)

    coerced_content = []
    for r_ind, row in enumerate(content):
        c_row = []
        for ind, col in enumerate(row):
            try:
                col = converters[ind](col)
            except ValueError:
                col = col
            c_row.append(col)
        coerced_content.append(c_row)
    return coerced_content
