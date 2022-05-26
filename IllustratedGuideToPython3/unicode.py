#20.2 Basic steps in Python
#Using Unicode characters (non ASCII) in 3 ways.
#copy and paste:
result = 'x²'
#using hex Unicode code point:
result2 = 'x\u00b2'
#using code point inside curly braces:
result3 = 'x\N{SUPERSCRIPT TWO}'
#results(proof):
print(result, result2, result3)


#20.3 Encoding
#encoding is taking human readable info and turning it into computer readable info
x_sq = 'x\u00b2'
x_sq.encode('utf-8') # returns: b'x\xc2\xb2

#When python doesnt support an encoding
#ASCII does not support the squared char:
x_sq.encode('ascii') #returns error message UnicodeEncodeError
#You can force python to encode anyways:
x_sq.encode('ascii', errors='ignore') #returns b'x'
#OR, replace inserts a ? where an unsupported char occurs
x_sq.encode('ascii', errors='replace') #returns b'x?'


#20.4 Decoding
#decoding takes bytes and creates Unicode from them (computer info to human info)
#UTF-8 byte sequence for x²:
utf8_bytes = b'x\xc2\xb2'
#to turn it into unicode:
text = utf8_bytes.decode('utf-8')
print(text) #prints 'x²'
#You must know the byte sequence the string was encoded as(in this case'utf-8') to decode it, else it will likely not
#decode correctly.

#Unicode and Files
# you can specify the encoding to use for a file or leave it out entirely, in which case the OS default will be used,
#likely UTF-8
with open('/tmp/sq.utf8', 'w') as fout:
    fout.write('x²')
with open('/tmp/sq.utf8', 'w', encoding='cp949') as fout:
    fout.write('x²')
#its better to specify the encoding when dealing with non ASCII characters, like an example 2, else the program could
# break on other computers that dont use your computers default by default.

