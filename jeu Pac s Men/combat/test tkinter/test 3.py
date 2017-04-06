import Tkinter
racine0=Tkinter.Tk()
fond0=Tkinter.Canvas(racine0, width=200, height=100, background='darkgray')
line0=fond0.create_line(30, 50, 170, 50, dash=(7, 2, 2, 2), dashoff=2)
fond0.pack()
racine0.mainloop()