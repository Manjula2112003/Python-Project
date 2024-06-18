#Tic -Tac-Toe
import tkinter.messagebox
from tkinter import *

play=Tk()
play.geometry('700x550')
play.title('Tic-Tac-Toe')
play.configure(bg='lightblue')

bclick=True
turns=0
buttons=StringVar()
def btnclick(buttons):
    global bclick, turns
    if buttons['text']=='' and bclick==True:
        buttons['text']= 'X'
        bclick = False
        turns += 1
        possibilities()
    elif buttons['text']=='' and bclick==False:
        buttons['text'] = '0'
        bclick = True
        turns += 1
        possibilities()
    else:
        tkinter.messagebox.showwarning('Tic -Tac-Toe','Buttons already clicked!..')

def possibilities():
    if (b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
            b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X' or
            b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X' or
            b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X' or
            b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X' or
            b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X' or
            b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X' or
            b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X'):
        tkinter.messagebox.showinfo('Tic-Tac-Toe',p1.get()+ 'Win!....')
    elif (b1['text'] == '0' and b2['text'] == '0' and b3['text'] == '0' or
            b4['text'] == '0' and b5['text'] == '0' and b6['text'] == '0' or
            b7['text'] == '0' and b8['text'] == '0' and b9['text'] == '0' or
\            b1['text'] == '0' and b4['text'] == '0' and b7['text'] == '0' or
            b2['text'] == '0' and b5['text'] == '0' and b8['text'] == '0' or
            b3['text'] == '0' and b6['text'] == '0' and b9['text'] == '0' or
            b1['text'] == '0' and b5['text'] == '0' and b9['text'] == '0' or
            b3['text'] == '0' and b5['text'] == '0' and b7['text'] == '0'):
        tkinter.messagebox.showinfo('Tic-Tac-Toe',p2.get()+ 'Win!....')
    elif turns == 9:
        tkinter.messagebox.showinfo('Tic-Tac-Toe','Match Draw')

Label(play, text='Tic-Tac-Toe', font=('calibri',25)).place(x=250,y=10)

Label(play,text='Player 1 Name :',font=('calibri',20), bg='lightblue').place(x=100,y=80)
Label(play,text='Player 2 Name :',font=('calibri',20), bg='lightblue').place(x=100,y=130)

p1 = StringVar()
p2 = StringVar()
Entry(play,textvariable=p1).place(x=300,y=80)
Entry(play,textvariable=p2).place(x=300,y=130)

b1=Button(play, text='',font=('calibri',20,'bold'), bg='blue',fg='White',width='8',
          height='2',command=lambda:btnclick(b1))
b1.place(x=130,y=200)

b2=Button(play, text='',font=('calibri',20,'bold'), bg='blue',fg='White',width='8',
          height='2',command=lambda:btnclick(b2))
b2.place(x=260,y=200)

b3=Button(play, text='',font=('calibri',20,'bold'), bg='blue',fg='White',width='8',
          height='2',command=lambda:btnclick(b3))
b3.place(x=390,y=200)

b4=Button(play, text='',font=('calibri',20,'bold'), bg='blue',fg='White',width='8',
          height='2',command=lambda:btnclick(b4))
b4.place(x=130,y=300)

b5=Button(play, text='',font=('calibri',20,'bold'), bg='blue',fg='White',width='8',
          height='2',command=lambda:btnclick(b5))
b5.place(x=260,y=300)

b6=Button(play, text='',font=('calibri',20,'bold'), bg='blue',fg='White',width='8',
          height='2',command=lambda:btnclick(b6))
b6.place(x=390,y=300)

b7=Button(play, text='',font=('calibri',20,'bold'), bg='blue',fg='White',width='8',
          height='2',command=lambda:btnclick(b7))
b7.place(x=130,y=400)

b8=Button(play, text='',font=('calibri',20,'bold'), bg='blue',fg='White',width='8',
          height='2',command=lambda:btnclick(b8))
b8.place(x=260,y=400)

b9=Button(play, text='',font=('calibri',20,'bold'), bg='blue',fg='White',width='8',
          height='2',command=lambda:btnclick(b9))
b9.place(x=390,y=400)
play.mainloop()


















