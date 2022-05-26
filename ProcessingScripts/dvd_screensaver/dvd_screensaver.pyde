y = 100
x = 100
xspeed = 2
yspeed = 2

def setup():
    size(800, 600)
    fill('#0099FF')
    textSize(50)
    
def draw():
    global y, yspeed, x, xspeed
    background('#000000')
    y += yspeed
    x += xspeed
    text('DVD', x, y)
    if y > height or y < 35:
        yspeed *= -1
    if x > width - 110 or x < 0:
        xspeed *= -1

        
