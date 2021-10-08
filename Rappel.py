import easygui as eg
import sys
import os
import csv
import datetime
import smtplib


def home():
    global menu;
    eg.msgbox('Lets Go on Homepage', 'Well Wisher Forever')
    menu=eg.buttonbox('Homepage', 'Well Wisher Forever', choices=['Add Birthday', 'Add Anniversery', 'Check Remainder', 'Exit'])
    if menu == 'Add Birthday':
        birthday()

    if menu == 'Add Anniversery':
        anniversery()

    if menu == 'Check Remainder':
        remainder()

    if menu == 'Exit':
        sys.exit()



def birthday():
    name=eg.enterbox('Enter  name : ', 'Well Wisher Forever')
    date=eg.enterbox('Enter Birth Date (YYYY-MM-DD) : ', 'Well Wisher Forever')
    mail=eg.enterbox('Enter Mail-Id : ', 'Well Wisher Forever')
    filename=os.path.normcase("b.txt")
    f=open(filename, "a")
    f.write(name)
    f.write(",")
    f.write(date)
    f.write(",")
    f.write(mail)
    f.write("\n")
    eg.msgbox('Birthday reminder Added Successfully..!', 'Well Wisher Forever')
    home()


def anniversery():
    name1=eg.enterbox('Enter Name 1 : ', 'Well Wisher Forever')
    name2=eg.enterbox('Enter Name 2 : ', 'Well Wisher Forever')
    dt=eg.enterbox('Enter the anniversery date : ', 'Well Wisher Forever')
    send=eg.enterbox('Enter the Mail-Id : ', 'Well Wisher Forever')
    filename1=os.path.normcase("a.txt")
    f1=open(filename1, "a")
    f1.write(name1)
    f1.write(" ")
    f1.write(name2)
    f1.write(",")
    f1.write(dt)
    f1.write(",")
    f1.write(send)
    f1.write("\n")
    eg.msgbox('Anniversery reminder Added Successfully..!', 'Well Wisher Forever')
    home()


def r_menu():
    global ch2
    ch2=eg.buttonbox('Menu to check Remainder', 'Well Wisher Forever',
                     choices=['Check remainder of birthday', 'Check remainder of anniversery', 'Homepage'])
    if ch2 == 'Homepage':
        home()


def emailbirthday():
    eg.msgbox('Birthday wishes sent on mail - ' + mail1)
    TO=mail1
    SUBJECT=username
    TEXT='Wish you many many Happy Returns of the day..!! HAPPY BIRTHDAY . May god bless you!!! '

    # Gmail Sign In
    # gmail_sender='rappelreminder@gmail.com'
    # gmail_passwd='@rappel30'

    gmail_sender='wellwisherforever24@gmail.com'
    gmail_passwd='Abhishek@7929'

    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY='\r\n'.join(['To: %s' % TO,
                      'From: %s' % gmail_sender,
                      'Subject: %s' % SUBJECT,
                      '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print('email sent')
    except:
        print('error sending mail')

    server.quit()


def emailanni():
    eg.msgbox('Anniversery wishes sent on mail - ' + mail2)
    TO=mail2
    SUBJECT=username
    TEXT='Wishing a perfect pair a perfectly happy day.Hope you find time to look back on all your sweet memories together.Happy Anniversery..!!!'

    # Gmail Sign In
    # gmail_sender='rappelreminder@gmail.com'
    # gmail_passwd='@rappel30'

    gmail_sender='wellwisherforever24@gmail.com'
    gmail_passwd='Abhishek@7929'

    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY='\r\n'.join(['To: %s' % TO,
                      'From: %s' % gmail_sender,
                      'Subject: %s' % SUBJECT,
                      '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print('email sent')
    except:
        print('error sending mail')

    server.quit()


def remainder():
    r_menu()
    if ch2 == 'Check reminder of birthday':
        x=[]
        y=[]
        z=[]
        global mail1
        with open('b.txt') as csvfile:
            check=0
            csvreader=csv.reader(csvfile, delimiter=',')
            for line in csvreader:
                x.append(line[0])
                y.append(line[1])
                z.append(line[2])

            currentDT=datetime.date.today()
            today=str(currentDT)
            eg.msgbox('Today date is ' + today)
            year, month, day=today.split("-")
            for i in range(len(y)):
                y1, m1, d1=y[i].split("-")
                if m1 == month and d1 == day:
                    check=1
                    eg.msgbox('Birthday today : ' + x[i], 'Well Wisher Forever')
                    mail1=z[i]
                    emailbirthday()
            if check == 0:
                eg.msgbox('No ones Birthday today', 'Well Wisher Forever')
        r_menu()

    if ch2 == 'Check remainder of anniversery':
        check1=0
        x1=[]
        y1=[]
        z1=[]
        global mail2
        with open('a.txt') as csvfile1:
            csvreader1=csv.reader(csvfile1, delimiter=',')
            for line1 in csvreader1:
                x1.append(line1[0])
                y1.append(line1[1])
                z1.append(line1[2])

            currentDT1=datetime.date.today()
            today_1=str(currentDT1)
            eg.msgbox('Today date is ' + today_1, 'Well Wisher Forever')
            year1, month1, day1=today_1.split("-")
            for j in range(len(y1)):
                y2, m2, d2=y1[j].split("-")
                if m2 == month1 and d2 == day1:
                    check1=1
                    eg.msgbox('Anniversery today : ' + x1[j], 'Well Wisher Forever')
                    mail2=z1[j]
                    emailanni()
            if check1 == 0:
                eg.msgbox('No ones Anniversery today', 'Well Wisher Forever')
        r_menu()


ans=eg.buttonbox('Hi..! Welcome , Do you want to start ?', 'Well Wisher Forever', choices=['Yes', 'No'])
if ans == 'Yes':
    global username
    username=eg.enterbox('Enter your name : ')
    home()

if ans == 'No':
    ch3=eg.ynbox('Are you sure you want to exit ? ', 'WARNING !');
    if ch3 == True:
        sys.exit()
    else:
        home()
