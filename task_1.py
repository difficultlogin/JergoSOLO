#!/usr/bin/env python3

def create_dict(key, value):
    dict = {}

    for x in range(len(key)):
        try:
            dict[key[x]] = value[x]
        except IndexError:
            dict[key[x]] = None

    return dict


if __name__ == '__main__':
    key = ['one_key', 'two_key', 'three_key', 'four_key']
    value = ['one_value', 'two_value', 'three_value']

    result = create_dict(key, value)
    print(result)
