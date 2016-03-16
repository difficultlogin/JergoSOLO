#!/usr/bin/env python3

import re

def get_ip(string):
    pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    r = re.compile(pattern)
    ip = r.match(string).group()

    return ip

def get_top_ip(log):
    ip_list = []

    with open(log) as file:
        for line in file:
            ip_list.append(get_ip(line))



    # return ip_list

# def get_top_ip(log):
#     ip_list = {}
#     elems = {}
#     e, em = None, 0
#
#     with open(log) as file:
#         for line in file:
#             ip = r.match(line).group()
#
#             try:
#                 ip_list[ip] += 1
#             except KeyError:
#                 ip_list.update({ip: 1})
#
#     for i in ip_list.keys():
#         elems[i] = t = elems.get(i, 0) + 1
#         if t > em:
#             e, em = i, t
#
#     return e


if __name__ == '__main__':
    from sys import argv
    print(get_top_ip(argv[1]))