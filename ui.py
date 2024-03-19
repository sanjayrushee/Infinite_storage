from tkinter import *

def button_clicked():
    print("Button clicked")

root = Tk()

# Load the image
bg = PhotoImage(file="background.png")

# Get the dimensions of the image
image_width = bg.width()
image_height = bg.height()

# Set the window size to match the image dimensions
root.geometry(f"{image_width}x{image_height}")

# Create a canvas widget
canvas = Canvas(root, width=image_width, height=image_height, highlightthickness=0)
canvas.pack()

# Add the background image to the canvas
canvas.create_image(image_width/2, image_height/2, image=bg)

# Load the transparent button image
button_image = PhotoImage(file="button.png")

# Create a button with the transparent image
button = Button(canvas, image=button_image, command=button_clicked, bd=0, highlightthickness=0, bg="#E7DBDB", activebackground="#E7DBDB")
button.place(x=263, y=373)

root.mainloop()
