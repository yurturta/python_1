#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
 name = input('Enter string\n')
 s=name.encode('utf-8')
 print(s.hex())
elif len(sys.argv) == 2:
 s=sys.argv[1].encode('utf-8')
 print(s.hex())
