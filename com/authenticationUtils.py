import requests

def get_authorization():
	s = requests.session()
	header2 = {'Content-Type': 'application/json;charset=UTF-8'}
	url2 = "http://account.saas.weimobqa.com/website/saas/account/api2/user/getCodeRs"
	data2 = {"zone": "0086", "phoneNumber": 18591324991, "pagename": "login"}
	s.post(url=url2, json=data2, headers=header2)

	header3 = {'Content-Type': 'application/json;charset=UTF-8'}
	url3 = "http://account.saas.weimobqa.com/website/saas/account/api2/user/login"
	data3 = {"zone": "0086", "phone": 18591324991, "password": '985c500d569110c18b31e6c1ca871ea6'}
	r3 = s.post(url=url3, json=data3, headers=header3)
	q3 = "Bearer " + r3.json()['data']['token']
	return q3