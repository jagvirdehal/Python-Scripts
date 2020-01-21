import smtplib
from time import sleep

person1 = {'Mishelle':'590149','Rafid':'751706','Salman':'575852','Mahika':'677395','Taaj':'561492','Ihit':'560503','Noor.B':'594930','Kunj':'567347','Amarvir':'564845','Yuvraj':'603264','Jagvir':'561448','Nour.E':'643856','Ashley':'640746','Arqum':'565770','Marzuk':'732425','Sukhbir':'662277','Dhruvil':'680390','Kabir':'645217','Dhavani':'722637','Hari':'563215','Karanvir':'561896','Sapinder':'565962','Ishaan':'793305','Tanvi':'741201','Aleena':'567481','Saniya':'635914','Pawandeep':'561899','Jasleen':'563588','Jagbir':'567310','Harneet':'694154','Johan':'583744','Ms. Malltezi':'P0069577'}
person2 = {'Mishelle':'590149','Rafid':'751706','Salman':'575852','Mahika':'677395','Taaj':'561492','Ihit':'560503','Noor.B':'594930','Kunj':'567347','Amarvir':'564845','Yuvraj':'603264','Jagvir':'561448','Nour.E':'643856','Ashley':'640746','Arqum':'565770','Marzuk':'732425','Sukhbir':'662277','Dhruvil':'680390','Kabir':'645217','Dhavani':'722637','Hari':'563215','Karanvir':'561896','Sapinder':'565962','Ishaan':'793305','Tanvi':'741201','Aleena':'567481','Saniya':'635914','Pawandeep':'561899','Jasleen':'563588','Jagbir':'567310','Harneet':'694154','Johan':'583744','Ms. Malltezi':'P0069577'}


FROM = 'jagvird216@gmail.com'
SUBJECT = "Secret Santa"
for i in sorted(list(person1)):
    TO = ['%s@pdsb.net' % person1[i]]
    del person1[i]
    p2 = list(person2)
    TEXT = "Ms.Malltezi's class Secret Santa!\n\nYou, %s, will be buying a gift for: %s\n\nDont tell anyone!!!" % (i,p2[0])
    del person2[p2[0]]
    message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
    server = smtplib.SMTP('smtp.gmail.com')
    server.starttls()
    server.login('jagvird216@gmail.com','wjotustrxrvurnpb')
    server.sendmail(FROM, TO, message)
    server.quit()
    print('y')
    sleep(3)
