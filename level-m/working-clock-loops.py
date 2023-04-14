seconds = codesters.Line(0, -15, 0, 15, "blue")
minutes = codesters.Line(0, -30, 0, 30, "red")
hours = codesters.Line(0, -60, 0, 60, "green")

def clock():
    num_seconds = 0
    
    while True:
        #seconds move 2 degrees every time we loop (loop is faster than 1 per second approximately 3x, so we have to take this into account).
        seconds.turn_right(2)
        
        #these aren't true seconds. They are approximately 0.333 seconds each, but it is easier to work with whole numbers.
        num_seconds += 1 
        
        #since 3x speed, use 180 seconds instead of 60 seconds
        if num_seconds % 180 is 0:
            minutes.turn_right(10)
            # with 3x speed, use 10800 seconds instead of 3600 seconds
            if num_seconds % 10800 is 0:
                hours.turn_right(30)
        
clock()