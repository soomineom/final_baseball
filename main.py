# -*- coding: utf-8 -*-

from tkinter import *
import datetime
import requests
from bs4 import BeautifulSoup

def createNewWindow():
  newWindow = Toplevel()
  newCanvas = Canvas(newWindow, height=400, width=600)
  newCanvas.pack()
  resultLabel = Label(newWindow, text = '<<{}월 {}일 오늘의 결과>>'.format(month, day)) #입력한 날짜로 바뀌게 수정 필요
  resultLabel.place(rely=0.03)
  vcLabel = Label(newWindow, text = '[승리한 Team]')
  vcLabel.place(rely=0.1)
  vcFrame = Frame(newWindow, bg='#eaeaea')
  vcFrame.place(relx=0.5, rely=0.15, relwidth=0.9, relheight=0.15, anchor='n')
  eLabel = Label(newWindow, text = '*자세한 경기 결과는 구단별 엠블럼 클릭')
  eLabel.place(rely=0.3)

  # 뉴스 크롤링
  def newsCrawler():
      webpage = requests.get('https://sports.news.naver.com/kbaseball/news/index.nhn?isphoto=N&type=popular')
      soup = BeautifulSoup(webpage.content, 'html.parser')
      news = soup.select(".aside_rank_news>ul> li > a > span")
      for k in range(10):
          news[k] = str(news[k].text)
      news_list = []
      for i in range(10):
          news_list.append(news[i])
      newsHead1 = Label(newsFrame, text="{}".format(news[0])).pack()
      newsHead2 = Label(newsFrame, text="{}".format(news[1])).pack()
      newsHead3 = Label(newsFrame, text="{}".format(news[2])).pack()
      newsHead4 = Label(newsFrame, text="{}".format(news[3])).pack()
      newsHead5 = Label(newsFrame, text="{}".format(news[4])).pack()
      newsHead6 = Label(newsFrame, text="{}".format(news[5])).pack()
      newsHead7 = Label(newsFrame, text="{}".format(news[6])).pack()
      newsHead8 = Label(newsFrame, text="{}".format(news[7])).pack()

  #뉴스 출력/프레임
  newsLabel = Label(newWindow, text = '<<{}월 {}일 오늘 실시간 인기뉴스>>'.format(month, day))
  newsLabel.place(rely=0.4)
  newsFrame = Frame(newWindow, bg='#eaeaea')
  newsFrame.place(relx=0.5, rely=0.45, relwidth=0.9, relheight=0.4, anchor='n')
  newsCrawler()


  buttonFrame = Frame(newWindow)
  buttonFrame.place(relx=0.2, rely=0.9, relwidth=0.8, relheight=0.05)
  moveButton = Button(buttonFrame, text = '다른 날 보기')
  moveButton.place(relwidth=0.5, relheight=1)
  exitButton = Button (buttonFrame, text = '닫기') #닫기 후 창 종료 필요
  exitButton.place(relx=0.7, relwidth=0.1, relheight=1)

#메인창
root = Tk()
root.title('Baseball Highlights')

canvas = Canvas(root, height=200, width=400)
canvas.pack()

today = datetime.date.today()
month = today.month
day = today.day

windowLabel = Label(root, text = '<<오늘은 {}월 {}일 입니다>>'.format(month, day))
windowLabel.place(relx=0.5, rely=0.3, anchor='n')

frame = Frame(root)
frame.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.1, anchor='n')

monthEntry = Entry(frame)
monthEntry.place(relwidth=0.2, relheight=1)
monthLabel = Label(frame, text = '월')
monthLabel.place(relx=0.2, relwidth=0.2, relheight=1)
dayEntry = Entry(frame)
dayEntry.place(relx=0.4, relwidth=0.2, relheight=1)
dayLabel = Label(frame, text = '일')
dayLabel.place(relx=0.6, relwidth=0.2, relheight=1)
goButton = Button(frame, text = 'Go!', command = createNewWindow)
goButton.place(relx=0.8, relwidth=0.2, relheight=1)

root.mainloop()
