import Tkinter
racine0=Tkinter.Tk()
fond0=Tkinter.Canvas(racine0, width=150, height=120, background='darkgray')
ligne1=fond0.create_line(75, 0, 75, 120)
ligne2=fond0.create_line(0, 60, 150, 60)
texte0=fond0.create_text(75, 60, text="Spam?", font="Arial 16 italic", fill="green")

fond0.pack()
racine0.mainloop()