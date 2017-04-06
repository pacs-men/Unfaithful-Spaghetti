import Tkinter

racine0=Tkinter.Tk()

fond0=Tkinter.Canvas(racine0, width=200, height=100, background='darkgray')
line0=fond0.create_line(30, 20, 170, 20, dash=(7, 1, 1, 1))
rectangle0=fond0.create_rectangle(30, 30, 170, 50, dash=(7, 2, 1, 2))
ellipse0=fond0.create_oval(30, 60, 170, 80, dash=(7, 2, 1, 2))
fond0.pack()

racine0.mainloop()