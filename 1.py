from tkinter import *
import datetime
import tkinter.font as tkfont


today = datetime.date.today()
month = today.month
day = today.day
answer = '<<오늘은 {}월 {}일 입니다>>'.format(month, day)


window = Tk()
window.title('Baseball Highlight')
window.geometry('320x80')

label1 = Label(window, text = '오늘은')
label1.configure(text = answer)
label1.grid(row = 0, column = 0)

month = Entry(window, width = 10).grid(row = 1, column = 0)
label_month = Label(window, text = '월').grid(row = 1, column = 1)
day = Entry(window, width = 10).grid(row = 1, column = 2)
label_day = Label(window, text = '일').grid(row = 1, column = 3)

go_button = Button(window, text = 'Go!')
go_button.grid(row = 1, column = 5)


window.mainloop()