def drawStart(): 
    import tkinter as tk
    from PIL import ImageGrab
    lastx, lasty = 0, 0
    
    
    def xy(event):
        "Takes the coordinates of the mouse when you click the mouse"
        global lastx, lasty
        lastx, lasty = event.x, event.y
    
    
    def addLine(event):
        """Creates a line when you drag the mouse
        from the point where you clicked the mouse to where the mouse is now"""
        global lastx, lasty
        canvas.create_line((lastx, lasty, event.x, event.y))
        # this makes the new starting point of the drawing
        lastx, lasty = event.x, event.y
    
    def save(event):
        x=root.winfo_rootx()+canvas.winfo_x()
        y=root.winfo_rooty()+canvas.winfo_y()
        x1=x+canvas.winfo_width()
        y1=y+canvas.winfo_height()
        im = ImageGrab.grab((x, y, x1, y1))
        im.save("captured.png")
    
    root = tk.Tk()
    root.geometry("800x600")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    
    canvas = tk.Canvas(root)
    canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    canvas.bind("<Button-1>", xy)
    canvas.bind("<B1-Motion>", addLine)
    root.bind("<Control-s>", save)
    
    root.mainloop()