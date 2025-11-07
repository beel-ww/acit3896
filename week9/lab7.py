import turtle
t = turtle.Turtle()
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

def koch_rec(level, length):
    if level == 0:
        t.forward(length)
    else:
        koch_rec(level - 1, length / 3)
        t.left(60)
        koch_rec(level - 1, length / 3)
        t.right(120)
        koch_rec(level - 1, length / 3)
        t.left(60)
        koch_rec(level - 1, length / 3)

def koch_snowflake(level, length):
    for _ in range(3):
        koch_rec(level, length)
        t.right(120)
      
koch_snowflake(4, 200)