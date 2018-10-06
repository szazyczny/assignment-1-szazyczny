# (20 points) The Drunkard’s Walk. A drunkard in a grid of streets randomly picks one of four 
# directions and stumbles to the next intersection, then again randomly picks one of four 
# directions, and so on. You might think that on average the drunkard doesn’t move very far 
# because the choices cancel each other out, but that is actually not the case.

# Write a function to calculate the distance after n intersections.

def drunkard_walk(x, y, n):
    """
    x, y: the original location
    n: the number of intersections(steps)
    return the distance after n intersections(steps) from the origin
    """
    pass


print("The drunkard started from (%d,%d)." % (x, y))
distance = drunkard_walk(x, y, n)
print("After", n, "intersections, he's",
      distance, "blocks from where he started.")
