

"""
Problem : How to check that names do not have non-alphanumeric characters?
"""


def doesnt_have_alphanumeric(value):
    list_value = convert_to_list(value)

    each_char = []
    for val in list_value:
        if val.isalnum():
            each_char.append(val)

    if len(each_char) == len(list_value):
        return f"{value} : The whole value is alphanumeric"
    else:
        if len(each_char) > 0:
            return f"{value} : The value contains alphanumeric and non-alphanumeric"
        else:
            return f"{value} : The whole value is non-alphanumeric"


def convert_to_list(string):
    list1 = []
    list1[:0] = string
    return list1


if __name__ == '__main__':
    print(doesnt_have_alphanumeric("123james456Martur!!@#@$"))