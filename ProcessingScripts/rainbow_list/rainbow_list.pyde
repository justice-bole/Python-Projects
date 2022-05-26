rainbow = ['blue','orange','yellow']
print(rainbow[0])
print(rainbow[1])
print(rainbow[2])

print(rainbow[-1])
print(rainbow[-2])
print(rainbow[0:2])

rainbow[0] = 'red'

print(rainbow)

rainbow.append('blue')
print(rainbow)

colors = ['indigo','violet']
rainbow.extend(colors)
print(rainbow)

yellowindex = rainbow.index('yellow')
print(yellowindex)

rainbow.insert(3, 'green')
print(rainbow)

rainbow.pop()
print(rainbow)

rainbow.extend(colors)
print(rainbow)
rainbow.remove('indigo')
print(rainbow)

size(500, 500)
noStroke()
background('#004477')
bands = [
 '#FF0000', # red
 '#FF9900', # orange
 '#FFFF00', # yellow
 '#00FF00', # green
 '#0099FF', # blue
 '#6633FF' # violet
]
# red band
translate(0, 100)
#fill(bands[0])
#rect(0, 0, width, 50)

#for band in bands:
for i, band in enumerate(bands):
    fill(band)
    rect(0, 0, width, 50)
    fill('#FFFFFF')
    textSize(25)
    text(i, 20, 35)
    translate(0, 50)
