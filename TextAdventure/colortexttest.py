import sys
from time import sleep

class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)
  
    def style_text(code):
        return "\33[{code}m".format(code=code)
  
    def color_text(code):
        return "\33[{code}m".format(code=code)

example_ansi = ANSI.background(
    97) + ANSI.color_text(31) + ANSI.style_text(4) + "This is the " + "end.\n"
print(example_ansi)