# -*- coding: utf-8 -*-

from tkinter import *
import datetime
import requests
from bs4 import BeautifulSoup
import urllib

def createNewWindow():
  newWindow = Toplevel()
  newCanvas = Canvas(newWindow, height=400, width=400)
  newCanvas.pack()
  titleLabel = Label(newWindow, text = '<<{}월 {}일 오늘의 일정/결과>>'.format(mm.get(), dd.get()))
  titleLabel.place(rely=0.03)
  resultFrame = Frame(newWindow, bg='#eaeaea')
  resultFrame.place(relx=0.5, rely=0.08, relwidth=0.9, relheight=0.3, anchor='n')
  resultLabel = Label(resultFrame, text = '[일정/결과]') #나중에 수정
  resultLabel.place(relx=0.5, rely=0.1, anchor='n') #나중에 수정

  # 뉴스 크롤링
  def newsCrawler():
      webpage = requests.get('https://sports.news.naver.com/kbaseball/news/index.nhn?isphoto=N&type=popular')
      soup = BeautifulSoup(webpage.content, 'html.parser')
      newsList = []
      for i in range(10):
          news = soup.select("#_ranking_news_list_0 > li:nth-child({0})".format(i))
          for ns in news:
              ns = str(ns)
              ns = re.sub('<.+?>', '', ns, 0).strip()
              newsList.append(ns)

      for k in range(len(newsList)):
        newsHead = Label(newsFrame, text="{}".format(newsList[k])).pack()


  #뉴스 출력/프레임
  newsLabel = Label(newWindow, text = '<<{}월 {}일 오늘 실시간 인기뉴스>>'.format(mm.get(), dd.get()))
  newsLabel.place(rely=0.4)
  newsFrame = Frame(newWindow, bg='#eaeaea')
  newsFrame.place(relx=0.5, rely=0.45, relwidth=0.9, relheight=0.4, anchor='n')
  newsCrawler()

  buttonFrame = Frame(newWindow)
  buttonFrame.place(relx=0.2, rely=0.9, relwidth=0.8, relheight=0.05)
  button1 = Button(buttonFrame, text='순위표 보기',command = therank)
  button1.place(relx=0, relwidth=0.3, relheight=1)
  button2 = Button(buttonFrame, text='닫기')
  button2.place(relx=0.5, relwidth=0.3, relheight=1)

#순위표창
def therank():
  rank = Toplevel()
  rankCanvas = Canvas(rank, height=400, width=400)
  rankCanvas.pack()
                  
#메인창
root = Tk()
root.title('2020 Baseball Highlights')

canvas = Canvas(root, height=200, width=400)
canvas.pack()

today = datetime.date.today()
month = today.month
day = today.day

windowLabel = Label(root, text = '<<오늘은 {}월 {}일 입니다>>'.format(month, day))
windowLabel.place(relx=0.5, rely=0.3, anchor='n')

frame = Frame(root)
frame.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.1, anchor='n')

dd = StringVar()
mm = StringVar()
monthEntry = Entry(frame, textvariable=mm)
monthEntry.place(relwidth=0.2, relheight=1)
monthLabel = Label(frame, text = '월')
monthLabel.place(relx=0.2, relwidth=0.2, relheight=1)
monthGet = monthEntry.get()

dayEntry = Entry(frame, textvariable=dd)
dayEntry.place(relx=0.4, relwidth=0.2, relheight=1)
dayLabel = Label(frame, text = '일')
dayLabel.place(relx=0.6, relwidth=0.2, relheight=1)
dayGet = dayEntry.get()

goButton = Button(frame, text = 'Go!', command = createNewWindow)
goButton.place(relx=0.8, relwidth=0.2, relheight=1)

root.mainloop()
