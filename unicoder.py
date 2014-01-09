#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
    print 'usage: %s <UNICODE CODE POINT HEX>' % (sys.argv[0])
    exit(1)

codepoint = int(sys.argv[1], 16)
print unichr(codepoint).encode('utf-8')