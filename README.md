# bin2html 900

convert .bin payloads to a single .html file for the 9.00 exploit removing the need for binloader/netcat etc allowing full offline caching.

the template.dat file is used to create all in one .html payload files

the jsreq-template.dat file is is used to create a .html payload file that still requires int64.js, rop.js and webkit.js this can be used to save space by not adding these scripts to the main payload.html file.


<b>usage:</b>

for all in one .html payloads:

bin2html.py [binfile]

<br>

for .html payloads that will require external .js:

bin2html.py [binfile] 1

<br>

<b>all in one example:</b>

bin2html.py AppToUsb.bin

<br>

<b>external .js example:</b>

bin2html.py AppToUsb.bin 1