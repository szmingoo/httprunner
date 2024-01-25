import os
import configparser

current_dir = os.path.split(os.path.realpath(__file__))[0]
config_path = os.path.abspath(os.path.join(current_dir, os.pardir)) + '\\config.ini'


class ReadConfig(object):
	def __init__(self):
		self.cf = configparser.ConfigParser()
		self.cf.read(config_path)

	def get_global_constant(self, section):
		my_dict = {}
		for key_name, value in self.cf.items(section):
			my_dict[key_name] = value
		return my_dict

	def get_sql_server_host(self):
		return self.cf.get("SqlServer", "host")

	def get_sql_server_port(self):
		return self.cf.get("SqlServer", "port")

	def get_sql_server_user(self):
		return self.cf.get("SqlServer", "user")

	def get_sql_server_pwd(self):
		return self.cf.get("SqlServer", "pwd")

	def get_mail_sender_from(self):
		return self.cf.get("MailSender", "from")

	def get_mail_sender_server(self):
		return self.cf.get("MailSender", "server")

	def get_mail_sender_port(self):
		return self.cf.get("MailSender", "port")

	def get_mail_sender_user(self):
		return self.cf.get("MailSender", "user")

	def get_mail_sender_pwd(self):
		return self.cf.get("MailSender", "pwd")

	def get_mail_recipient(self):
		for item in self.cf.items("MailReceiver"):
			recipient = self.cf.get("MailReceiver", item[0])
			yield recipient
