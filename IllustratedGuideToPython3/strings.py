character='a'
with_quote="Iain'tgonna"
longer="""Thisstringhas
...multiplelines
...init"""
latin='''Lorumipsum
...dolor'''
escaped='Iain\'tgonna'
zero_chars=''
unicode_snake="Ilove\N{SNAKE}"


name = "Justice"
age = 26
print(name, "is", age)

paragraph = "\"Python is a great language!\", said Fred. \"I don't ever remember having this much fun before.\""
print(paragraph)
# omega unicode hex 03A9
unicode_omega1 = "Unicode name: \N{GREEK CAPITAL LETTER OMEGA}"
print(unicode_omega1)

unicode_omega2 = "Unicode point: \u03A9"
print(unicode_omega2)

item = "car"
cost = 13499.99
print("{:<10}".format(item), "{:>10,}".format(cost))