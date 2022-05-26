import sys
from time import sleep

class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)
  
    def style_text(code):
        return "\33[{code}m".format(code=code)
  
    def color_text(code):
        return "\33[{code}m".format(code=code)
  
words = '''
There is no hope to survive.
You have run out of supplies and the cold has taken your limbs. 
'''
for char in words:
    sleep(.02)
    sys.stdout.write(char)
    sys.stdout.flush()

words2 = "This is the "
for char in words2:
    sleep(.15)
    sys.stdout.write(char)
    sys.stdout.flush()


  
example_ansi = ANSI.color_text(31) + "end.\n"
for char in example_ansi:
    sleep(.15)
    sys.stdout.write(char)
    sys.stdout.flush()