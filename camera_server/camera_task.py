import numpy as np
import cv2
import datetime
import time
import smtplib
import configparser
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

_PATH = '../video_cap/resources/trained_models/haarcascade_frontalface_default.xml'
config_path = 'config.ini'


# Read config file
config = configparser.ConfigParser()
config.read_file(config_path)

# Initialize email sending
server_addr = config.get('email', 'server')
port = config.get('email', 'port')
username = config.get('email', 'username')
password = config.get('email', 'password')
fromaddr = config.get('email', 'fromaddr')
toaddr = config.get('email', 'toaddr')

def send_notification(img_name):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "SOMEBODY JUST STOLE YOUR CARROTS"

    body = "Somebody just tried to steal your carrots. Pics or it didn't happen, you say? I attached them."
    msg.attach(MIMEText(body, 'plain'))
    img_data = open('static/images/{img_name}.png'.format(img_name=img_name), 'rb').read()
    msg.attach(MIMEImage(img_data, name=img_name))

    text = msg.as_string()
    server = smtplib.SMTP(server_addr, port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
# Initialize camera
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    try:
        cut_frame = frame[0:480, 0:640]
        # cut_frame = frame[self.x_min:self.x_max, self.y_min:self.y_max]
        frame[0:480, 0:640] = frame
        # frame[self.x_min:self.x_max, self.y_min:self.y_max] = frame
        face_haar_cascade = cv2.CascadeClassifier(_PATH)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_haar_cascade.detectMultiScale(gray, 1.3, 5)
        detected = False
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            detected = True
        if detected:
            print("Face detected!!!")
            ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            cv2.imwrite("static/images/face_{timestmp}.png".format(timestmp=ts), frame)
            send_notification("face_{timestmp}.png".format(timestmp=ts))
            detected = False
        cv2.imshow('frame', frame)
    except cv2.error:
        print("Improperly defined resolution bounds or parameter values")
        break
    if cv2.waitKey(600) >= 0:
        break
cap.release()
cv2.destroyAllWindows()