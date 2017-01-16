import requests
from CaptchaParser import CaptchaParser
from bs4 import BeautifulSoup  as bs
from PIL import Image
from StringIO import StringIO

ses=requests.session()
def parse(reg,p):
 
 o=ses.get('https://vtop.vit.ac.in/student/captcha.asp')
 co=o.cookies.get_dict()
 img = Image.open(StringIO(o.content))

 username=reg
 pas=p
 parser=CaptchaParser()
 captcha=parser.getCaptcha(img)
 login=dict(regno=username,passwd=pas,vrfcd=captcha,message='')
 P=ses.post('https://vtop.vit.ac.in/student/stud_login_submit.asp',data=login)
def home():
  h=ses.get('https://vtop.vit.ac.in/student/home.asp')
  return h.text

def timetable():
  time=ses.get('https://vtop.vit.ac.in/student/course_regular.asp?sem=WS')
  time=ses.get('https://vtop.vit.ac.in/student/course_regular.asp?sem=WS')
  return time.text

def attendance(f,to):
  attendance=ses.get('https://vtop.vit.ac.in/student/attn_report.asp?sem=WS&fmdt='+f+'&todt='+to)
  return attendance.text
