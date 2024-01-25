# coding=utf-8

import sys
import time
import smtplib
import os
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from com import configUtils

sys.path.append("../..")
sys.path.append("..")

def find_report():
	currentdir = os.path.split(os.path.realpath(__file__))[0]
	result_dir = os.path.abspath(os.path.join(currentdir, os.pardir)) + '\\reports\\'
	result_lists = os.listdir(result_dir)
	result_lists.sort(
			key=lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not os.path.isdir(result_dir + "\\" + fn) else 0)
	file_new = os.path.join(result_dir, result_lists[-1])
	file_name = str(result_lists[-1])
	return file_new, file_name


def attach_file(msgRoot, file_new, file_name):
	part = MIMEBase('application', "octet-stream")
	part.set_payload(open(file_new, 'rb').read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file_name))
	msgRoot.attach(part)


def send_mail():
	cf=configUtils.ReadConfig()
	report_new = find_report()[0]
	report_name = find_report()[1]
	mail_from = cf.get_mail_sender_from()  # 邮箱帐号
	smtp_server = cf.get_mail_sender_server()
	port = cf.get_mail_sender_port()
	mail_to = [receiver for receiver in cf.get_mail_recipient()]
	file_report = open(report_new, 'rb')
	mail_body = file_report.read()
	file_report.close()
	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = u"自动化测试报告"
	msgRoot['From'] = str(mail_from)
	msgRoot['To'] = str(mail_to)
	# msgText = MIMEText("用例执行情况见附件HTML文件", _subtype = 'html', _charset = 'utf-8')
	msgText = MIMEText(mail_body, _subtype='html', _charset='utf-8')
	msgRoot['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
	msgRoot.attach(msgText)
	attach_file(msgRoot, report_new, report_name)
	try:
		smtp = smtplib.SMTP()
		smtp.connect(smtp_server)
		smtp.login(cf.get_mail_sender_user(), cf.get_mail_sender_pwd())
	except:
		smtp = smtplib.SMTP_SSL(smtp_server, port)
		smtp.login(cf.get_mail_sender_user(), cf.get_mail_sender_pwd())
	smtp.sendmail(mail_from, mail_to, msgRoot.as_string())
	smtp.quit()
