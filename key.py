"""
Returns a dictionary of the keyboard 
mapped to its ord() value.

string DATA
    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    hexdigits = '0123456789abcdefABCDEF'
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    octdigits = '01234567'
    printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU...
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    whitespace = '\t\n\x0b\x0c\r '
"""
import string
import curses

class Key():

    def __init__(self):
        self.key = {}
        for k in string.printable:
            self.key[k] = ord(k)
        for k in dir(curses):
            if 'KEY_' in k:
                name = k.split('_')[1].lower()
                self.key[name] = getattr(curses, k)
        return

key = Key().key
