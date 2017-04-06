import Tkinter
racine0=Tkinter.Tk()
racine0.title("Regardez au centre!")
fond0=Tkinter.Canvas(racine0, width=350, height=200, background='darkgray')
ligne0=fond0.create_line(100, 100, 101, 100)
fond0.pack()
racine0.mainloop()