def create_meteor():
    global meteors
    meteor = codesters.Sprite("meteor1", -300, random.randint(-220, 220))
    meteor.set_size(0.5)
    meteor.set_x_speed(5)
    meteors.append(meteor)