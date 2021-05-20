from tkinter import *


dritare=Tk()
dritare.title('Kalkulatori')


numratdheOperatoret = ''
barazimet = StringVar()

labeli2 = Label(dritare, barazimet.set('Degeri yazin:'), textvariable = barazimet, font = ('Arial', 24))
labeli2.grid(row = 1, columnspan = 2)

def ButonKliko(numer):
    global numratdheOperatoret
    numratdheOperatoret = numratdheOperatoret + str(numer)
    barazimet.set(numratdheOperatoret)

def ButoniBarazimit():
    global numratdheOperatoret
    totali = str(eval(numratdheOperatoret))
    barazimet.set(totali)

def ButoniFshi():
    global numratdheOperatoret
    numratdheOperatoret = ''
    barazimet.set('')


butoni1 = Button(dritare, text = 1, bg = 'orange', fg = 'black', width = 3, command = lambda: ButonKliko(1))
butoni1.grid(column = 1, row = 3, padx = 10, pady = 10)
butoni2 = Button(dritare, text = 2, bg = 'orange', fg = 'black', width = 3, command = lambda: ButonKliko(2))
butoni2.grid(column = 3, row = 3, padx = 10, pady = 10)
butoni3 = Button(dritare, text = 3, bg = 'orange', fg = 'black', width = 3, command = lambda: ButonKliko(3))
butoni3.grid(column = 5, row = 3, padx = 10, pady = 10)
butoni4 = Button(dritare, text = 4, bg = 'orange', fg = 'black', width = 3, command = lambda: ButonKliko(4))
butoni4.grid(column = 1, row = 4, padx = 10, pady = 10)
butoni5 = Button(dritare, text = 5, bg = 'orange', fg = 'black', width = 3, command = lambda: ButonKliko(5))
butoni5.grid(column = 3, row = 4, padx = 10, pady = 10)
butoni6 = Button(dritare, text = 6, bg = 'orange', fg = 'black', width = 3, command = lambda: ButonKliko(6))
butoni6.grid(column = 5, row = 4, padx = 10, pady = 10)
butoni7 = Button(dritare, text = 7, bg = 'orange', fg = 'black', width = 3, command = lambda: ButonKliko(7))
butoni7.grid(column = 1, row = 5, padx = 10, pady = 10)
butoni8 = Button(dritare, text = 8, bg = 'orange', fg = 'black', width = 3, command = lambda: ButonKliko(8))
butoni8.grid(column = 3, row = 5, padx = 10, pady = 10)
butoni9 = Button(dritare, text = 9, bg = 'orange', fg = 'black', width = 3, command = lambda: ButonKliko(9))
butoni9.grid(column = 5, row = 5, padx = 10, pady = 10)
butoni0 = Button(dritare, text = 0, bg = 'orange', fg = 'black', width = 3, command = lambda: ButonKliko(0))
butoni0.grid(column = 3, row = 6, padx = 10, pady = 10)
butoniC = Button(dritare, text = 'C', bg = 'orange', fg = 'black', width = 3, command = lambda: ButoniFshi())
butoniC.grid(column = 1, row = 6, padx = 10, pady = 10)
butoniBaraz = Button(dritare, text = '=', bg = 'orange', fg = 'black', width = 3, command = lambda: ButoniBarazimit())
butoniBaraz.grid(column = 5, row = 6, padx = 10, pady = 10)
butoniPlus = Button(dritare, text = '+', bg = 'orange', fg = 'black', width = 3, command = lambda: ButonKliko('+'))
butoniPlus.grid(column = 7, row = 3, padx = 10, pady = 10)
butoniZbritje = Button(dritare, text = '-', bg = 'orange', fg = 'black', width = 3, command = lambda: ButonKliko('-'))
butoniZbritje.grid(column = 7, row = 4, padx = 10, pady = 10)
butoniShumezim = Button(dritare, text = '*', bg = 'orange', fg = 'black', width = 3, command = lambda: ButonKliko('*'))
butoniShumezim.grid(column = 7, row = 5, padx = 10, pady = 10)
butoniPjesetim = Button(dritare, text = '/', bg = 'orange', fg = 'black', width = 3, command = lambda: ButonKliko('/'))
butoniPjesetim.grid(column = 7, row = 6)
dritare.mainloop()
