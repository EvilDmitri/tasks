# -*- coding: utf-8 -*-
import sys


def test(email):
    if not u'@' in email:
        return False
    parts = email.split(u'@')
    if len(parts) > 2 or not parts[0]:
        return False
    head = parts[0]
    tail = parts[1]
    if u'.' in head:
        return False
    if not head.isalnum():
        return False
    if u'.' in tail:
        domain = tail.split(u'.')
        if len(domain) > 2 or not domain[0] or not domain[1]:
            return False
        if not domain[0].isalnum() or not domain[0].isalnum():
            return False
        return True


def main():
    while True:
        email = raw_input("Type a email (q - quit): ").rstrip('\n')
        if email == 'q':
            print 'Good Bye!'
            sys.exit(1)

        if test(email):
            print 'VALID'
        else:
            print 'INVALID'


if __name__ == '__main__':
    main()