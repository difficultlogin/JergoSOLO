#!/usr/bin/env python

from itertools import izip_longest

yandex  = []
mail    = []
gmail   = []
rambler = []

for x in open('email.csv'):
    data = x.split(',')
    domain = data[0].split('@')[1]

    if domain == 'mail.ru':
        mail.append((data[0], data[1]))
    if domain == 'ya.ru':
        yandex.append((data[0], data[1]))
    if domain == 'gmail.com':
        gmail.append((data[0], data[1]))
    if domain == 'rambler.ru':
        rambler.append((data[0], data[1]))

def sorting_doamin(domain_arr):
    sentinel = object()
    return [list(x for x in item if x is not sentinel) for item in
            izip_longest(*domain_arr, fillvalue=sentinel)]

print sorting_doamin([yandex, mail, gmail, rambler])
