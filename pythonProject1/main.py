# -*- coding: utf-8 -*-
# author: 华测-长风老师

from system.BeautifulReport.BeautifulReport import BeautifulReport
# 1、使用BeautifulReport 调用
import unittest


suite = unittest.TestLoader().discover("./testcases/", pattern="test*.py")
result = BeautifulReport(suite)
result.verbosity = 2
result.report(filename="run_by_BeautifulReport.html", description="CF测试报告", log_path="./reports")
