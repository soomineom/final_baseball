# -*- coding: utf-8 -*-
from tkinter import *
import datetime
import requests
from bs4 import BeautifulSoup
import urllib

def createNewWindow():
    newWindow = Toplevel()
    newCanvas = Canvas(newWindow, height=500, width=800)
    newCanvas.pack()
    titleLabel = Label(newWindow, text='<<{}월 {}일 오늘의 일정/결과>>'.format(mm.get(), dd.get()))
    titleLabel.place(rely=0.02)

    #일정/결과 크롤링
    year_s = str(year)
    month_noZero = str(month)
    month_s = '0' + month_noZero
    day_s = str(day)
    date = year_s + month_s + day_s

    m = mm.get()
    d = dd.get()

    def get_result():
        url = 'https://sports.news.naver.com/kbaseball/schedule/index.nhn?date={}&month={}&year=2020&teamCode='.format(
            date, m)
        webpage = requests.get(url)
        soup = BeautifulSoup(webpage.content, 'html.parser')

        results1 = soup.select(
            '#calendarWrap > div:nth-child({0}) > table > tbody > tr:nth-child(1) > td:nth-child(3)'.format(d))
        resList1 = []
        for res in results1:
            res = str(res)
            res = re.sub('<.+?>|\n', '', res, 0).strip()
            resList1.append(res)
        results2 = soup.select(
            '#calendarWrap > div:nth-child({0}) > table > tbody > tr:nth-child(2) > td:nth-child(2)'.format(d))
        resList2 = []
        for res in results2:
            res = str(res)
            res = re.sub('<.+?>|\n', '', res, 0).strip()
            resList2.append(res)
        results3 = soup.select(
            '#calendarWrap > div:nth-child({0}) > table > tbody > tr:nth-child(3) > td:nth-child(2)'.format(d))
        resList3 = []
        for res in results3:
            res = str(res)
            res = re.sub('<.+?>|\n', '', res, 0).strip()
            resList3.append(res)
        results4 = soup.select(
            '#calendarWrap > div:nth-child({0}) > table > tbody > tr:nth-child(4) > td:nth-child(2)'.format(d))
        resList4 = []
        for res in results4:
            res = str(res)
            res = re.sub('<.+?>|\n', '', res, 0).strip()
            resList4.append(res)
        results5 = soup.select(
            '#calendarWrap > div:nth-child({0}) > table > tbody > tr:nth-child(5) > td:nth-child(2)'.format(d))
        resList5 = []
        for res in results5:
            res = str(res)
            res = re.sub('<.+?>|\n', '', res, 0).strip()
            resList5.append(res)

        final_res = []
        final_res.append(resList1)
        final_res.append(resList2)
        final_res.append(resList3)
        final_res.append(resList4)
        final_res.append(resList5)
        for i in range(len(final_res)):
            schLabel = Label(resultFrame, text="{}".format(",".join(map(str,final_res[i])))).pack()

    resultFrame = Frame(newWindow, bg='#eaeaea')
    resultFrame.place(relx=0.5, rely=0.08, relwidth=0.9, relheight=0.25, anchor='n')
    get_result()

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
            newsHead = Label(newsFrame, text="{}".format(newsList[k])).grid(row=k, column=0)
            newsButton = Button(newsFrame, text='보기').grid(row=k, column=1)


    # 뉴스 출력/프레임
    newsLabel = Label(newWindow, text='<<{}월 {}일 오늘 실시간 인기뉴스>>'.format(mm.get(), dd.get()))
    newsLabel.place(rely=0.35)
    newsFrame = Frame(newWindow, bg='#eaeaea')
    newsFrame.place(relx=0.5, rely=0.41, relwidth=0.9, relheight=0.48, anchor='n')
    newsCrawler()

    buttonFrame = Frame(newWindow)
    buttonFrame.place(relx=0.2, rely=0.91, relwidth=0.8, relheight=0.05)
    button1 = Button(buttonFrame, text='순위표 보기',command = theRank)
    button1.place(relx=0, relwidth=0.3, relheight=1)
    button2 = Button(buttonFrame, text='닫기', command = root.quit)
    button2.place(relx=0.5, relwidth=0.3, relheight=1)

#순위표창
def theRank():
  rank = Toplevel()
  rankCanvas = Canvas(rank, height=400, width=400)
  rankCanvas.pack()
  rankFrame = Frame(rank)
  rankFrame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.9, anchor='n')

  def showRank(): #순위표 출력
    url = 'https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo&year=2020'
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'html.parser')

    rankList = []
    for i in range(11):
        ranking = soup.select('#regularTeamRecordList_table > tr:nth-child({0}) > td.tm'.format(i))
        for ra in ranking:
            ra = str(ra)
            ra = re.sub('<.+?>', '', ra, 0).strip()
            rankList.append(ra)

    rankNumList = []
    for k in range(1, 11, 1):
        rankNum = soup.select('#regularTeamRecordList_table > tr:nth-child({0}) > th'.format(k))
        for rn in rankNum:
            rn = str(rn)
            rn = re.sub('<.+?>', '', rn, 0).strip()
            rankNumList.append(rn)

    rankLabel1 = Label(rankFrame, text="[현재 순위]").pack()
    for k in range(len(rankList)): #순위출력
        rankLabel2 = Label(rankFrame, text="{}위: {}".format(rankNumList[k],rankList[k])).pack()
  showRank()


# 메인창
root = Tk()
root.title('2020 Baseball Highlights')

canvas = Canvas(root, height=200, width=400)
canvas.pack()

today = datetime.date.today()
year = today.year
month = today.month
day = today.day

windowLabel = Label(root, text='<<오늘은 {}월 {}일 입니다>>'.format(month, day))
windowLabel.place(relx=0.5, rely=0.3, anchor='n')

frame = Frame(root)
frame.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.1, anchor='n')

dd = StringVar()
mm = StringVar()
monthEntry = Entry(frame, textvariable=mm)
monthEntry.place(relwidth=0.2, relheight=1)
monthLabel = Label(frame, text='월')
monthLabel.place(relx=0.2, relwidth=0.2, relheight=1)
monthGet = monthEntry.get()

dayEntry = Entry(frame, textvariable=dd)
dayEntry.place(relx=0.4, relwidth=0.2, relheight=1)
dayLabel = Label(frame, text='일')
dayLabel.place(relx=0.6, relwidth=0.2, relheight=1)
dayGet = dayEntry.get()

goButton = Button(frame, text='Go!', command=createNewWindow)
goButton.place(relx=0.8, relwidth=0.2, relheight=1)

root.mainloop()
