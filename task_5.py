#!/usr/bin/env python

from urllib2 import urlopen
from xml.etree import ElementTree as etree

id_eur = 'R01239'
id_usd = 'R01235'

course_eur = ''
course_usd = ''

request = urlopen("https://www.cbr.ru/scripts/XML_daily.asp", timeout=20)

parse = etree.parse(request)
course_eur = parse.findtext('.//Valute[@ID="'+id_eur+'"]/Value')
course_usd = parse.findtext('.//Valute[@ID="'+id_usd+'"]/Value')

print('Course EUR: %s\nCourse USD: %s' % (course_eur, course_usd))