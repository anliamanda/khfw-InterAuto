# -*- coding:utf-8 -*-
"""
@Time:2022/11/21 10:04 上午
@Auth:amanda
@Function:请输入模块功能描述
"""
import allure
import pytest
import yaml

from api.type import class_Type
from testCase.testBase import TestBase


@allure.feature("课后服务类型")
class Testcase(TestBase):
	classtype = class_Type()
	id=""
	@allure.title("查询课后服务类型")
	@pytest.mark.parametrize("name", ["","兴趣"])
	@pytest.mark.run(order=1)
	def test_searchType(self, name):
		assert self.classtype.search_type(name)["success"] == True
	
	@allure.title("新增课后服务类型")
	@pytest.mark.parametrize("name,source", yaml.safe_load(open("./config/type.yaml"))["saveType"])
	@pytest.mark.run(order=2)
	def test_saveType(self, name,source):
		try:
		  assert self.classtype.save_type(name,source)["success"] == True
		except Exception as e:
		  self.log.error(e)
		 
	
	@allure.title("修改课后服务类型")
	@pytest.mark.parametrize("name,source", [("test",2)])
	@pytest.mark.run(order=3)
	def test_updateType(self,name,source):
		Testcase.id=self.classtype.search_type("test1")["data"]["records"][0]["id"]
		assert self.classtype.update_type(name,source,Testcase.id)["success"] == True
		
  
	@allure.title("删除课后服务类型")
	@pytest.mark.run(order=4)
	#@pytest.mark.skip
	def test_delClassRoom(self):

		assert self.classtype.delete_type(str(Testcase.id))["success"] == True
		
		
	
