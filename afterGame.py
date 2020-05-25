from tkinter import *
import datetime

window = Tk()
window.title('경기 결과')

today = datetime.date.today()
month = today.month
day = today.day
answer1 = '<<{}월 {}일 오늘의 결과>>'.format(month, day)
answer2 = '<<{}월 {}일 오늘의 주요뉴스>>'.format(month, day)

label1 = Label(window)
label1.configure(text = answer1)
label1.pack()

label2 = Label(window, text = '[승리한 Team]').pack()
label3 = Label(window, text = '*자세한 결과는 구단별 이미지 클릭!').pack()

label4 = Label(window)
label4.configure(text = answer2)
label4.pack()

otherday_bt = Button(window, text = '다른 날 보기').pack()
close_bt = Button(window, text = '닫기').pack()

window.mainloop()
