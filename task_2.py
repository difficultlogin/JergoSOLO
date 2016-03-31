#!/usr/bin/env python

import re

def validate_login(login):
    main_pattern = r'^[a-zA-Z]([-.a-zA-Z0-9]*[a-zA-Z0-9])?$'

    if 0 < len(login) <= 20:
        if re.match(main_pattern, login):
            return True

    return False

if __name__ == '__main__':
    login = 'test-l12_3o.gin2'
    print(validate_login(login))