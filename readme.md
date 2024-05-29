# Nginx Config File parser

Parse nginx files with pypeg and create groff ms file to generate pdf

## How to use

1. Put your ```nginx.conf``` in the input directory (name the file exactly nginx.conf and only have this file in the folder, nothing else!)
2. Run ```docker compose up```
3. Your output will be generated in the output directory (will contain: ```output_xml.xml```, the parsed xml file; ```output_groff.ms```, the groff ms file; ```docu.pdf```, the generated pdf)

## Why does this use docker?

Because groff is used to create the pdf file. Groff is already installed in most distros but not installable on Windows. Using Docker you only need to have it installed. We can also avoid version conflicts with Python.

## How does the docker compose work

1. The first stage runs the python files ```main.py``` which parses the ```nginx.conf``` and ```groff.py``` which creates a file with groff ms macros to generate a pdf out of.
2. The second stage installs groff (this is why the image is so big, groff (or rather gropdf) doesnt work under alpine linux because of musl libc and glibc issues) and created the pdf
