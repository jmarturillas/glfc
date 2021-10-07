

"""
Problem : How to check that numbers are displayed with commas?
"""


def does_contain_comma(num):

    if "," in num:
        splitted_1 = num.split(",")

        for split in splitted_1:
            if split.isnumeric():
                return f"{num} : Value is numeric and has comma"
    else:
        if num.isnumeric():
            return f"{num} : Value is numeric but doesn't contain comma"
        else:
            if "." in num:
                splitted_2 = num.split(".")
                for split in splitted_2:
                    if split.isnumeric():
                        return f"{num} : Value is numeric but has no comma"
                    else:
                        return f"{num} : Value is not numeric"


if __name__ == '__main__':
    print(does_contain_comma("1,000,0000.00"))
    print(does_contain_comma("james.marturillas"))