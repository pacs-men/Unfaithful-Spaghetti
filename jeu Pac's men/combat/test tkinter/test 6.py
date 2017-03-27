import Tkinter
racine0=Tkinter.Tk()
fond0=Tkinter.Canvas(racine0, width=350, height=200, background='darkgray')
rectangle0=fond0.create_rectangle(50, 40, 300, 90)
ellipse0=fond0.create_oval(30, 120, 150, 180)
quartier0=fond0.create_arc(160, 130, 230, 200, start=30, extent=120, style=Tkinter.PIESLICE)
arc0=fond0.create_arc(250, 130, 320, 200, start=30, extent=120, style=Tkinter.CHORD)
fond0.pack()
racine0.mainloop()