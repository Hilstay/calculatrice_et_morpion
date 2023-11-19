from tkinter import *

expression = ''
def affichernum(touche):
    global expression
    if touche == "=":
        calculer()
    if not touche == "=":
        expression += str(touche)
        equation.set(expression)
    
def calculer():
    try:
        global expression
        calcule = str(eval(expression))
        expression = calcule
        equation.set(calcule)
    except:
        expression = "erreur"
        equation.set(expression)

def effacer():
    global expression
    expression = ""
    equation.set(expression)

win = Tk()
win.geometry('330x510')
equation = StringVar()
affiche = Label(win,fg="black", bg="white", textvariable=equation, height=4)
affiche.grid( row=0, column=1)

buttons = (7, 8, 9, "/",6, 5, 4, "*",3, 2, 1, "+",".",0,",","=")
colone = 0
ligne = 1
for button in buttons:
    b = Label(win,bg="lightblue", fg='black', text=button, width=10, height=5)
    b.bind('<Button-1>', lambda e, bouton = button:  affichernum(bouton))
    b.grid(row=ligne, column=colone)
    colone += 1
    if colone == 4:
        ligne += 1
        colone = 0

b = Label(win, bg="red", fg="white", text="effacer",width=40, height=4)
b.bind('<Button-1>', lambda e, :  effacer())
b.grid(row=5, columns=4)

win.mainloop()