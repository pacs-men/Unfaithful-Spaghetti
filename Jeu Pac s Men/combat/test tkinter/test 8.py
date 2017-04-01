import Tkinter
racine0=Tkinter.Tk()
fond0=Tkinter.Canvas(racine0, width=150, height=150, background='darkgray')
polygone0=fond0.create_polygon(35, 105, 120, 85, 95, 25, 80, 75, 25, 60, 65, 30, fill="cyan", width=5, outline='black')
fond0.pack()
racine0.mainloop()