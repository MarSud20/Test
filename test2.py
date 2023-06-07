#import Python Packages
import tkinter
import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
from tkinter import *
from pandastable import Table


#connection to mysql
connection = mysql.connector.connect(user='root', password='qwer123', host='localhost', database = 'sql-project')

#create object
mycursor=connection.cursor()

#ask server for data
mycursor.execute("select day, month, numbers_of_sale from project")
result = mycursor.fetchall


#create lists for data
day = []
month = []
numbers_of_sale = []

#download data in lists
for i in mycursor:
    day.append(i[0])
    month.append(i[1])
    numbers_of_sale.append(i[2])

#create data by pandas
def stats():
    df = pd.DataFrame({"day": day,
                  "numbers_of_sale": numbers_of_sale})
    frame=tkinter.Frame(root)
    frame.pack(fill='x')

    pt = Table(frame, dataframe=df)
    pt.show()




#create visualization by tkinter
root = Tk()

root.title('Stats by MarSud20')
root.geometry("300x400")
root.config(background='white')

label = tkinter.Label(root, text="Hello user!", font=('Arial',18), bg='white')
label.pack(padx=20,pady=20)


#create visualization by matplotlib
def graph():
    plt.bar(day, numbers_of_sale)
    plt.ylim(0, 6)
    plt.xlabel("Dzień sprzedaży")
    plt.ylabel("Sprzedaż")
    plt.title("Tygodniowy wynik sprzedaży")
    plt.show()


#create columns
buttonframe = tkinter.Frame(root)
buttonframe.columnconfigure(0, weight=1)

#create switch button dark/light mode
def switch_bg():
    current_bg = root.cget('background')

    if current_bg == 'white' :
        new_bg = 'black'
        new_let = 'white'
    else:
        new_bg = 'white'
        new_let = 'black'
    root.config(bg=new_bg)
    btn1.configure(bg=new_bg, fg=new_let)
    btn2.configure(bg=new_bg, fg=new_let)
    btn3.configure(bg=new_bg, fg=new_let)
    btn4.configure(bg=new_bg, fg=new_let)
    label.configure(bg=new_bg, fg=new_let)

#create buttons in columns
btn1 = tkinter.Button(buttonframe, text="Wykres słupkowy sprzedaży", font=('Arial',15), command=graph, bg='white')
btn1.grid(row=0, column=0, sticky=tkinter.W+tkinter.E)

btn2 = tkinter.Button(buttonframe, text="Tabela", font=('Arial',15), command=stats, bg='white')
btn2.grid(row=1, column=0, sticky=tkinter.W+tkinter.E)

btn3 = tkinter.Button(buttonframe, text="Dark Mode", font=('Arial',15), command= switch_bg, bg='white')
btn3.grid(row=2, column=0, sticky=tkinter.W+tkinter.E)

btn4 = tkinter.Button(buttonframe, text="Wyjdź", font=('Arial',15), command=quit, bg='white')
btn4.grid(row=3, column=0, sticky=tkinter.W+tkinter.E)

buttonframe.pack(fil='x')





root.mainloop()









