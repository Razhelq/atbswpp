import smtplib, random, schedule, time


chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
people_emails = ['', '', '']
prev_chores = {}
for person in people_emails:
    prev_chores[person] = []

def send_mail():

    smtp_obj = smtplib.SMTP()
    smtp_obj.connect('smtp.gmail.com', '587')
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.login('', '')

    for chore in chores:
        person = random.choice(people_emails)
        if chore not in prev_chores[person]:
            prev_chores[person].append(chore)
        print(prev_chores)
        smtp_obj.sendmail('', person, chore)

    smtp_obj.quit()

schedule.every().sunday.at('10:00').do(send_mail)

while True:
    schedule.run_pending()
    time.sleep(1)