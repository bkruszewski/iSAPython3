import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

message = "Welcome"
messages = ["Hello", "Cześć", "Good job"]

def click():
    global message
    message = random.choice(messages)

def draw(canvas):
    canvas.draw_text(message, [50, 112], 48, "Yellow")

frame = simplegui.create_frame("Python :)", 300, 200)

frame.add_button("Click me", click)

frame.set_draw_handler(draw)
frame.se

frame.start()
