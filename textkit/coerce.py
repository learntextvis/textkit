
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


CONVERTERS = {'IntType': lambda x: int(x),
              'FloatType': lambda x: float(x),
              'StringType': lambda x: x}


def pick_type(types):
    ''' if there is only one type found
    in a column, then use that. if multiple
    types are found, default back to string.
    '''
    type_set = set(types)
    if len(type_set) == 1:
        return list(type_set)[0]
    elif set(['IntType', 'FloatType']) == type_set:
        # if there is a mix of floats and ints, then the column is floats.
        return 'FloatType'
    else:
        return 'StringType'


def get_column_types(content):
    ''' Figure out what type of content is in each column
    of a csv-like input. This is a simple brute force method that
    attempts to convert the strings of the content into floats and ints.
    if the conversion is successful for all rows tested,
    that type is considered the type of the column.
    '''

    # number of rows to check for content
    test_count = min(len(content), 5)

    # number of columns
    col_count = len(content[0])

    all_types = [[] for i in range(col_count)]

    for r_ind in range(test_count):
        for col_ind, col in enumerate(content[r_ind]):
            if isint(col):
                all_types[col_ind].append('IntType')
            elif isfloat(col):
                all_types[col_ind].append('FloatType')
            else:
                all_types[col_ind].append('StringType')

    # find if conversions are consistent across rows
    column_types = [pick_type(types) for types in all_types]
    return column_types


def coerce_types(content):
    '''
    Convert types in csv-like content.
    The idea is that when translating to and
    from csv, everything is converted to strings. So, we need to undo that
    conversion for things like counts.
    '''
    if len(content) == 0:
        return content

    column_types = get_column_types(content)

    coerced_content = []
    for row in content:
        c_row = []
        for col_ind, col in enumerate(row):
            try:
                col = CONVERTERS[column_types[col_ind]](col)
            except ValueError:
                col = col
            c_row.append(col)
        coerced_content.append(c_row)
    return coerced_content
