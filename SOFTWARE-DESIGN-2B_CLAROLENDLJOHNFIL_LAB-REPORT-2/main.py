from tkinter import *
import random

ws = Tk()
ws.title('ATM Machine')
ws.geometry('600x400')
ws.config(bg='#5671A6')

ranNum = (1020)
chance = 3
var = IntVar()
disp = StringVar()

def check_guess():
    global ranNum
    global chance
    usr_ip = var.get()
    if chance > 0:
        if usr_ip == ranNum:
            msg = f'LOGIN SUCCESSFUL!'
        elif usr_ip > ranNum:
            chance -= 1
            msg = f'ERROR!! You have {chance} attempt left.'
        elif usr_ip < ranNum:
            chance -= 1
            msg = f'ERROR!!. You have {chance} attempt left.'
        else:
            msg = 'LOGIN ERROR!'
    else:
        msg = f'LOGIN ERROR! CALLING THE POLICE'

    disp.set(msg)


Label(
    ws,
    text='ATM Machine',
    font=('sans-serif', 20),
    relief=SOLID,
    padx=10,
    pady=10,
    bg='#F27D16'
).pack(pady=(10, 0))

Entry(
    ws,
    textvariable=var,
    font=('sans-serif', 18)
).pack(pady=(50, 10))

Button(
    ws,
    text='LOGIN',
    font=('sans-serif', 18),
    command=check_guess
).pack()

Label(
    ws,
    textvariable=disp,
    bg='#5671A6',
    font=('sans-serif', 14)
).pack(pady=(20,0))


ws.mainloop()