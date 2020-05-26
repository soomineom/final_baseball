# -*- coding: utf-8 -*-

from tkinter import *
import datetime
today = datetime.date.today()

def createNewWindow():
  newWindow = Toplevel()
  newWindowLabel = Label(newWindow, text='오늘의 결과')
  newWindowLabel.grid()
  newWindow.geometry('320x320')
  
  
window = Tk()
window.title('Baseball Highlight')
window.geometry('320x80')

windowLabel = Label(window, text = '오늘은 _월 _일 입니다.')
windowLabel.grid()

monthEntry = Entry(window, width=10)
dayEntry = Entry(window, width=10)
monthLabel = Label(window, text='월')
dayLabel = Label(window, text='일')
goButton = Button(window, text = 'Go!', command = createNewWindow)

monthEntry.grid(row=1, column=0)
monthLabel.grid(row=1, column=1)
dayEntry.grid(row=1, column=2)
dayLabel.grid(row=1, column=3)
goButton.grid(row=1, column=5)

window.mainloop()