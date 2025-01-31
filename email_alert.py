# email_alert.py
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import config

def send_email(subject, message):
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['From'] = Header(config.SMTP_USER)
    msg['To'] = Header(config.RECIPIENT_EMAIL)
    msg['Subject'] = Header(subject, 'utf-8')

    try:
        with smtplib.SMTP_SSL(config.SMTP_SERVER, config.SMTP_PORT) as server:
            server.login(config.SMTP_USER, config.SMTP_PASSWORD)
            server.sendmail(config.SMTP_USER, [config.RECIPIENT_EMAIL], msg.as_string())
        print("邮件发送成功")
    except Exception as e:
        print(f"邮件发送失败: {e}")
