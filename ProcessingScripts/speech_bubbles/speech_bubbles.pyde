size(562, 768)
art = loadImage('561px-Van_Eyck_-_Arnolfini_Portrait.jpg')
image(art, 0, 0, width, height)

wait = 3000

def printAnswer():
    print(' ------------------ ')
    print('| The answer is 42! |')
    print('| ----------------- ')
    print('|/')
    
print('1. What do you get if you multiply six by seven?')
delay(wait)
printAnswer()

delay(wait/2)
print('2. How many US gallons are there in a barrel of oil?')
delay(wait)
printAnswer()

def speechBubble(x, y, txt='Hello', type='speech'):
 #x = 190
 #y = 150
 #txt = 'Check out my hat!'
 noStroke()
 pushMatrix()
 translate(x, y)
 
 # tail
 if type == 'speech':
    fill('#FFFFFF')
    beginShape()
    vertex(0, 0) # tip
    vertex(15, -40)
    vertex(35, -40)
    endShape(CLOSE)
 elif type == 'thought':
     fill('#FFFFFF')
     circle(0, 0, 8)
     circle(10, -20, 20)
 
 # bubble
 textSize(15)
 by = -85
 bw = textWidth(txt)
 pad = 20
 rect(0, by, bw+pad*2, 45, 10)
 fill('#000000')
 textAlign(LEFT, CENTER)
 text(txt, pad, by+pad)
 
 popMatrix()
 
def shout(txt):
 return txt.upper() + '!!!'
 
speechBubble(190, 150, shout('Check out my hat'))
speechBubble(315, 650, 'Woof')
speechBubble(445, 125, 'Meh', 'thought')
