from tkinter import *

text_label = None

def create_text(root):
    global text_label  
    max_height = 150
    fixed_width = 480

    text_content = "Your text goes here."

    text_label = Label(root, text=text_content, wraplength=fixed_width, justify="left", background="#E7DBDB")
    text_label.place(x=580, y=380)

    num_lines = len(text_content.split('\n'))

    font_size = 20  
    while font_size < 100:  
        text_label.config(font=("Helvetica", font_size))
        text_label.update_idletasks()  
        text_label_width = text_label.winfo_reqwidth()
        text_label_height = text_label.winfo_reqheight()

        if text_label_height > max_height or text_label_width > fixed_width:
            font_size -= 1 
            text_label.config(font=("Helvetica", font_size))
            text_label.update_idletasks()  
            text_label_width = text_label.winfo_reqwidth()
            text_label_height = text_label.winfo_reqheight()

        else:
            break

def button_clicked():
    global text_label 
    text_label.config(text="Button clicked")

root = Tk()
root.title("Voice Assistant")

bg = PhotoImage(file="background.png")

image_width = bg.width()
image_height = bg.height()

root.geometry(f"{image_width}x{image_height}")

canvas = Canvas(root, width=image_width, height=image_height, highlightthickness=0)
canvas.pack()

canvas.create_image(image_width/2, image_height/2, image=bg)

create_text(root)

button_image = PhotoImage(file="button.png")
button = Button(canvas, image=button_image, command=button_clicked, bd=0, highlightthickness=0, bg="#E7DBDB", activebackground="#E7DBDB")
button.place(x=276, y=354)

root.mainloop()
