import Tkinter
racine0=Tkinter.Tk()
fond0=Tkinter.Canvas(racine0, width=350, height=200, background='darkgray')
fond0.pack()
ligne=fond0.create_line(40, 190, 250, 110, 270, 170, 180, 120)
racine0.mainloop()