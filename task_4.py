#!/usr/bin/env python

import re

def get_ip(string):
    pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    r = re.compile(pattern)
    ip = r.match(string).group()

    return ip

def get_top_ip(log):
    ip_list = {}

    with open(log) as file:
        for line in file:
            ip = get_ip(line)

            try:
                ip_list[ip] += 1
            except KeyError:
                ip_list.update({ip: 1})

    sort_func = lambda x: x[1]
    result = sorted(ip_list.items(), key=sort_func, reverse=True)
    return result[0:5]


if __name__ == '__main__':
    from sys import argv
    print(get_top_ip(argv[1]))