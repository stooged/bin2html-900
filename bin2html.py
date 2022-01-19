#!/usr/bin/python3

import os
import sys
import binascii
import template
try:filename = sys.argv[1]
except:sys.exit(".bin file required\n\nExample: bin2html.py payload.bin")
try:jsreq =sys.argv[2]
except:jsreq = ''
payloadjs = "var payload=["
filesize = os.stat(filename).st_size
with open(filename, 'rb') as f:
    chnk = f.read(4)
    while chnk:
        output = binascii.hexlify(chnk[::-1])
        payloadjs = payloadjs + "0X%s," % output.decode('utf-8')
        chnk = f.read(4)
payloadjs = payloadjs[:-1] + "];"
f.close()
if len(jsreq) > 0:
    tempdata= template.JSREQ_TEMPLATE()
else: 
    tempdata= template.FULL_TEMPLATE()
indextmp = tempdata.replace('##PAYLOAD##', payloadjs)
f = open(filename.replace('.bin','.html'), 'w+', encoding="utf-8") 
f.write(indextmp)
f.close()