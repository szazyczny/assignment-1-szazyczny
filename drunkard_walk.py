# (20 points) The Drunkard’s Walk. A drunkard in a grid of streets randomly picks one of four 
# directions and stumbles to the next intersection, then again randomly picks one of four 
# directions, and so on. You might think that on average the drunkard doesn’t move very far 
# because the choices cancel each other out, but that is actually not the case.

# Write a function to calculate the distance after n intersections.

import random
# direction = [1, 2, 3, 4] # 1 = N, 2 = S, 3 = E, 4 = W
# print(random.choice(direction))
def drunkard_walk(x, y, n):
    """
    x, y: the original location
    n: the number of intersections(steps)
    return the distance after n intersections(steps) from the origin
    """
    iteration = n
    while iteration <= n:
        distance = 0
        if iteration > 0:
            for i in range(n):
                direction = ['N', 'S', 'E', 'W']
                i = random.choice(direction)
                if i == 'N':
                    y += 1
                elif i == 'S':
                    y -= 1
                elif i == 'E':
                    x += 1
                else:
                    x -= 1
            iteration -= 1
            distance = distance + abs(y) + abs(x)
        return distance

# print(drunkard_walk(0, 0, 6))

print("The drunkard started from (%d,%d)." % (0, 0))
distance = drunkard_walk(0, 0, 6)
n = 6
print("After", n, "intersections, he's",
      distance, "blocks from where he started.")

# print("The drunkard started from (%d,%d)." % (x, y))
# distance = drunkard_walk(x, y, n)
# print("After", n, "intersections, he's",
#       distance, "blocks from where he started.")



# (20 points) Use Turtle to draw the drunkard's walk in #3.

import turtle
import math

def draw_drunkard_walk(t, x, y, n):
    """
    x, y: the original location
    n: the number of intersections(steps)
    draw using turtle
    """  
    iteration = n
    yn = 0
    ys = 0
    xe = 0
    xw = 0
    if iteration > 0:
        for i in range(n):
            direction = ['N', 'S', 'E', 'W']
            i = random.choice(direction)
            if i == 'N':
                yn += 1
            elif i == 'S':
                ys += 1
            elif i == 'E':
                xe += 1
            else:
                xw += 1
        iteration -= 1
        t.fd(yn)
        t.bk(ys)
        t.right(xe)
        t.left(xw)


jack = turtle.Turtle()

draw_drunkard_walk(jack, 0, 0, 6)

turtle.mainloop()