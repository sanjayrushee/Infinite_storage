from tkinter import *

# Define text_label globally
text_label = None

def create_text(root):
    global text_label  # Make text_label accessible globally
    # Define maximum height and width for the text label
    max_height = 150
    fixed_width = 480

    # Define a placeholder text for the label
    text_content = "Your text goes here."

    # Create a label to display the text
    text_label = Label(root, text=text_content, wraplength=fixed_width, justify="left", background="#E7DBDB")
    text_label.place(x=580, y=380)

    # Calculate the number of lines required based on the text length
    num_lines = len(text_content.split('\n'))

    # Calculate the font size dynamically to fit within the maximum height
    font_size = 20  # Initial font size
    while font_size < 100:  # Limiting the font size to avoid infinite loop
        text_label.config(font=("Helvetica", font_size))
        text_label.update_idletasks()  # Update the label to get the actual size
        text_label_width = text_label.winfo_reqwidth()
        text_label_height = text_label.winfo_reqheight()

        if text_label_height > max_height or text_label_width > fixed_width:
            font_size -= 1  # Decrease font size if it exceeds maximum height or width
            text_label.config(font=("Helvetica", font_size))
            text_label.update_idletasks()  # Update the label with the new font size
            text_label_width = text_label.winfo_reqwidth()
            text_label_height = text_label.winfo_reqheight()

        else:
            break

def button_clicked():
    global text_label  # Access the global text_label
    # Change the text label content when the button is clicked
    text_label.config(text="Button clicked")

root = Tk()
root.title("Voice Assistant")

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

# Create text
create_text(root)

# Create a button
button_image = PhotoImage(file="button.png")
button = Button(canvas, image=button_image, command=button_clicked, bd=0, highlightthickness=0, bg="#E7DBDB", activebackground="#E7DBDB")
button.place(x=276, y=354)

root.mainloop()
