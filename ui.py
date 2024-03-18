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

# Create a canvas widget with background color
canvas = Canvas(root, width=image_width, height=image_height, bg="#D06F6F")
canvas.pack()

# Add the image to the canvas
canvas.create_image(0, 0, anchor=NW, image=bg)

# Load the button image
button_image = PhotoImage(file="button.png")

# Create a button with the image
button = Button(canvas, image=button_image, command=button_clicked, bd=0, highlightthickness=0, )
button.place(x=263, y=373)

root.mainloop()
