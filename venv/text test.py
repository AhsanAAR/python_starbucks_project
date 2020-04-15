import tkinter as tk  # python 3
# import Tkinter as tk  # python 2

def populate(frame):
    '''Put in some fake data'''
    col = [['Username', 'Password', 'starCard', 'email', 'Username', 'Password', 'starCard', 'email', 'Username',
            'Password', 'starCard', 'email'],
           ['okok', 'nice', 'niklasdfjklasdjfklasjdfklce', 'okok', 'nice', 'niklasdfjklasdjfklasjdfklce', 'okok',
            'nice', 'niklasdfjklasdjfklasjdfklce']]
    for i in range(len(col)):  # Rows
        for j in range(len(col[i])):  # Columns
            b = tk.Label(frame, text=col[i][j])
            b.grid(row = i, column = j)

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()
canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
frame = tk.Frame(canvas, background="#ffffff")
vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
hsb = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)
canvas.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)

vsb.pack(side="right", fill="y")
hsb.pack(side="bottom", fill="x")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

populate(frame)

root.mainloop()