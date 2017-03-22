# -*- coding: utf-8 -*-

nonascii = bytearray(range(0x00, 0x20))
with open('d.frp','rb') as infile, open('d_parsed.txt','wb') as outfile:
    for line in infile: # b'\n'-separated lines (Linux, OSX, Windows)
        line = line.replace("Arial", "")
        a= line.find((chr(0)+chr(2)+chr(0)))
        b= line.find((chr(255)+chr(255)+chr(255)))
        print a,b
        if a==14:
            line=line[0:33]+line[b:-1]

        line = line.replace((chr(0)+chr(2)+chr(0)), "   ")

        line = line.replace(chr(255), " ")

        outfile.write(line.translate(None, nonascii))
        outfile.write("\n")