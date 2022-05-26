y = 1
x = 1

def setup():
    print(y)
    size(500, 500)
    noFill()
    stroke('#FFFFFF')
    strokeWeight(3)

def draw():
    global y
    global x
    y += 1
    x += 1
    background('#004477')
    circle(x, y, 50)
    if y > 500 or y < 0:
        y = 0
    if x > 500 or x < 0:
        x = 0
        
