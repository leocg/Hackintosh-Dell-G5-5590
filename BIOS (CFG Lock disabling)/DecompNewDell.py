#This script finds the compressed data embedded in a Dell BIOS update program
#and decompresses it to an apparent HDR file. The main data seems to start
#at offset 0x58 in the HDR FWIW


import zlib
import sys
import re
import binascii


if(len(sys.argv) < 2 or sys.argv[1] == "-h"):
	print ("usage: python DecompNewDell.py <biosupdate.exe>")
	exit()


f = open(sys.argv[1], "rb")


string = f.read()


#The 0x789C at the end is the zlib header.
#It's necessary to check for that too because the string
#appears a couple times in the file.
pat = re.compile(rb'.{4}\xAA\xEE\xAA\x76\x1B\xEC\xBB\x20\xF1\xE6\x51.{1}\x78\x9C')
match = pat.search(string)


#Once you find that string, the first 4 bytes are the little endian
#size of the compressed data. The span will give you the starting
#offset into the file where it is found
(start_match, end_match) = match.span()
#print match.span()
compessed_len = string[start_match:start_match+4]


#Now switch the order around since it's little endian
#and also convert it to a hex string
compessed_len = binascii.b2a_hex(compessed_len[::-1])
#and then make it a proper number (separate lines for clarity)
compessed_len = int(compessed_len, 16)


#read len bytes out of the file into the new string to decompress
f.seek(start_match+16)
string = f.read(compessed_len)


o = zlib.decompress(string)


f2 = open(sys.argv[1] + "_decompressed.hdr", "wb")
f2.write(o)
f.close()
f2.close()
print ("Decompressed data written to %s_decompressed.hdr" % sys.argv[1])