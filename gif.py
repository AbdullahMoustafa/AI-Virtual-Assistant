from tkinter import *
import time
import os
window = Tk()

photo_path2 = "C:\\Users\\Abdullah\\Desktop\\AI virtual Assistance\\Genio\\circle.gif"

frames = [PhotoImage(file=photo_path2,format = 'gif -index %i' %(i)) for i in range(100)]

def update(ind):

    frame = frames[ind]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label = Label(window)
label.pack()
window.after(0, update, 0)

window.mainloop()






