from tkinter import *
import datetime

today = datetime.date.today()

window = Tk()
window.title('Baseball Highlight')

label = Label(window, text = '오늘의 날짜:')
#label.grid(row = 1, column = 1)
label.pack()

month = Entry(window, width = 20)
#month.grid(row = 2, column = 1)
month.pack()
day = Entry(window, width = 20)
#day.grid(row = 2, column = 2)
day.pack()
go_button = Button(window, text = 'Go!')
#go_button.grid(row = 2, column = 3)
go_button.pack()

window.mainloop()
