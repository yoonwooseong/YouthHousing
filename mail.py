import smtplib
from email.mime.text import MIMEText
from mailAccount import EMAIL, PASSWORD

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# smtp.ehlo()
# smtp.starttls()
smtp.login(EMAIL, PASSWORD)

msg = MIMEText('테스트')
msg['Subject'] = '테스트'
msg['To'] = 'dntjd851@naver.com'
smtp.sendmail(EMAIL, 'dntjd851@naver.com', msg.as_string())

smtp.quit()
