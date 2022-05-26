import json
jsondata = open('coffees.json')
coffees = json.load(jsondata)

#print(coffees[8]['ingredients'][1]['quantity']) # 40

size (800, 800)
background('#957a6a')
mug = 120
spacing = 230
col = 1
translate(100, 100)


for coffee in coffees:
    # ingredients code goes here
    #print(coffee['name'])
    pushMatrix()
    translate(0, mug)
    for ingredients in coffee['ingredients']:
        coffee_color = ingredients['color']
        coffee_amount = ingredients['quantity']
        fill(coffee_color)
        noStroke()
        rect(0, 0, mug, -coffee_amount)
        translate(0, -coffee_amount)
    popMatrix()
    

    
    #mug
    strokeWeight(5)
    stroke('#FFFFFF')
    noFill()
    square(0, 0, mug)
    arc(mug, mug/2, 40, 40, -HALF_PI, HALF_PI)
    arc(mug, mug/2, 40, 40, -HALF_PI, HALF_PI)
    
    # label
    fill('#FFFFFF')
    textSize(16)
    label = coffee['name']
    text(label, mug/2-textWidth(label)/2, mug+40)
    
    if col == 3:
        translate(spacing*-2, spacing)
        col = 1
    else:
        translate(spacing, 0)
        col +=1
