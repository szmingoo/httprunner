import pymysql
from com import configUtils

def operate_mysql(sql):
	cf=configUtils.ReadConfig()
	conn = pymysql.connect(
		host=cf.get_sql_server_host(),
		port=int(cf.get_sql_server_port()),
		user =cf.get_sql_server_user(),
		password =cf.get_sql_server_pwd(),
		charset ="utf8"
	)
	cu = conn.cursor()
	cu.execute(sql)
	res = cu.fetchall()
	cu.close()
	conn.close()
	return res[0][0]

# print(operate_mysql("select m.material_id from d_o2o_merchant.wecom_material m where m.pid=280 limit 1"))