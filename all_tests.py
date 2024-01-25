from httprunner.api import HttpRunner
from httprunner.report import gen_html_report

import os
import shutil
import sys
from com import sendEmail

# sys.path.append("../..")
# sys.path.append("..")

# def clear_dir(*dir):
# 	for i in range(len(dir)):
# 		for entry in os.scandir(dir[i]):
# 			if entry.name.startswith('.'):
# 				continue
# 			if entry.is_file():
# 				os.remove(entry.path)
# 			else:
# 				shutil.rmtree(entry.path)
#
# current_dir = os.path.split(os.path.realpath(__file__))[0]
# report_dir = current_dir + "\\reports"
# logs_dir = current_dir + "\\logs"
# clear_dir(report_dir)
# clear_dir(logs_dir)


summary = []
run = HttpRunner()
summary.append(run.run(path_or_tests="testsuite"))
for i in summary:
	gen_html_report(i)


# har2case test_login_demo.har -2y
# locusts -f test_get_demo.yml
# hrp run xuexi/test_extract.yml --gen-html-report
# httprunner make testsuite











# sendEmail.send_mail()

# summary.append(run.run(path_or_tests="testcases/DeleteMaterialCASE.yml"))
# # hrun testsuites\crm_testsuite.yml --log-file logs\crm.log --log-level debug








