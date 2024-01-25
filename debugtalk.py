import random
import string
from com import mysqlUtils
from com import authenticationUtils
from com.configUtils import ReadConfig as rc

def authorization():
	return authenticationUtils.get_authorization()

def assert_sql(sql, value):
	print(sql)
	print("value:",value)
	key_value = jdbc(sql)
	print("key_value:",key_value)
	if value == key_value:
		return "成功"
	else:
		return "失败"


def jdbc(sql):
	return mysqlUtils.operate_mysql(sql)


def global_constant(var):
	rc().get_global_constant(var)


def random_str(length):
	str_list = [random.choice(string.digits + string.ascii_letters) for i in range(length)]
	s = ''.join(str_list)
	return s


def to_int(arg):
	return int(arg)


def to_str(arg):
	return '''"%s"'''%str(arg)

#传空则返回空
def request(*args):
	if args:
		return args[0]
	return

from dateutil.parser import parse

def to_time_str(arg):
	return '''"%s"'''%str(parse(str(arg)))


def to_time(arg):
	return str(parse(str(arg)))