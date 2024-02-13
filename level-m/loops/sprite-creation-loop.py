def sprite_creation(x, y):
    sprite = codesters.Sprite("person1", x, y)
    
for num in range(4):
    x = random.randint(-220, 220)
    y = random.randint(-220, 220)
    sprite_creation(x, y)