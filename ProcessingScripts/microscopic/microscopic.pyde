class Amoeba(object):
    
    def circlePoint(self, t, r):
        x = cos(t) * r
        y = sin(t) * r
        return [x, y]
    
    def __init__(self, x, y, diameter):
        print('amoeba intitialized')
        self.x = x
        self.y = y
        self.d = diameter
        self.nucleus = {
        'fill': ['#FF0000', '#FF9900', '#FFFF00',
        '#00FF00', '#0099FF'][int(random(5))],
        'x': self.d * random(-0.15, 0.15),
        'y': self.d * random(-0.15, 0.15),
        'd': self.d / random(2.5, 4)
        }
        
    def display(self):
        # nucleus
        fill(self.nucleus['fill'])
        noStroke()
        circle(
        self.x + self.nucleus['x'], 
        self.y + self.nucleus['y'], 
        self.nucleus['d']
        )
        # cell membrane
        fill(0x880099FF)
        stroke('#FFFFFF')
        strokeWeight(3)
        circle(self.x, self.y, self.d)

a1 = Amoeba(400, 200, 100)

def setup():
 size(800, 400)
 frameRate(120)
def draw():
 background('#004477')
 a1.display()
