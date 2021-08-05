import tkinter

w = 480
h = 270
root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=w, height=h)
canvas.pack()

def render(c):
    c.create_rectangle(0, 0, w, h, outline="#000", fill="#000")  # Reset the canvas to black

    # https://tkdocs.com/tutorial/canvas.html
    # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html

    points = [100, 200, 100, 100, 200, 100, 150,
    150, 200, 200]
    canvas.create_polygon(points, outline='#000',
    fill='#b3c', width=2)

    c.update()

render(canvas)

root.mainloop()