import pandas as pd
import datetime
import smtplib

#Enter Authentication Details
GMAIL_ID = 'Your Gmail ID'
GMAIL_PSWD = 'Your Password'


def sendEmail(to,sub,msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}")
    s= smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)

    s.sendmail(GMAIL_ID, to, f"subject: {sub}\n\n{msg}")
    s.quit()



if __name__ == "__main__":
    # sendEmail(GMAIL_ID, 'subject','test message')
    df = pd.read_excel("data.xlsx")
    # print(df)
    today =datetime.datetime.now().strftime("%d-%m")
    yearNow= datetime.datetime.now().strftime("%Y")
    # print(today)
    writeInd = []
    for index, item in df.iterrows():
        print(index, item['Birthday'])
        bday =item['Birthday'].strftime("%d-%m")
        print(bday)
        if (today == bday) and yearNow not in str(item['Year']):
            sendEmail(item['Email'], "Happy Birthday", item['Dialogue'])
            writeInd.append(index)


    print(writeInd)
    for i in writeInd:
        yr= df.loc[i,'Year']
        df.loc[i, 'Year']= str(yr) +', '+str(yearNow)
        print(df.loc[i,'Year'])    
    print(df)
    df.to_excel('data.xlsx', index=False)