# bin2html 900

convert .bin payloads to a single .html file for the 9.00 exploit removing the need for binloader/netcat etc allowing full offline caching.


<br><br>

<b>usage:</b>

for all in one .html payloads:

```
bin2html [binfile]
```

<br>

for .html payloads that will require external .js:

```
bin2html [binfile] 1
```

<br><br>

<b>all in one example:</b>

```
bin2html AppToUsb.bin
```

<br>

<b>external .js example:</b>

```
bin2html AppToUsb.bin 1
```