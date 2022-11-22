# -*- coding:utf-8 -*-
"""
@Time:2022/11/17 2:19 下午
@Auth:amanda
@Function:测试用例
"""
import pytest
import yaml

from api.classroom import class_Room

import allure

from testCase.testBase import TestBase


@allure.feature("教室信息")

class Testcase(TestBase):
	classroom=class_Room()
	
	
	@pytest.fixture()
	def data(self):
		return ["test教室","test教室1"]
	
  
	@allure.title("查询教室")
	@pytest.mark.parametrize("roomName", yaml.safe_load(open("./config/classroom.yaml"))["search"])
	@pytest.mark.run(order=1)
	#@pytest.mark.skip
	def test_search(self,roomName):
		self.log.info("查询教室testcase")
		assert self.classroom.search_classRoom(roomName)["success"] ==True
	
	#@pytest.mark.skip
	@allure.title("新增教室")
	@pytest.mark.parametrize("roomName", yaml.safe_load(open("./config/classroom.yaml"))["save"])
	@pytest.mark.run(order=2)
	def test_save(self,roomName):
		assert self.classroom.save_classRoom(roomName)["success"] ==True


  
	@allure.title("更新教室")
	#@pytest.mark.skip
	@pytest.mark.parametrize("roomName",  yaml.safe_load(open("./config/classroom.yaml"))["update"])
	@pytest.mark.run(order=3)
	def test_update(self,roomName,data):
		id = self.classroom.search_classRoom(data[0])["data"][0]["id"]
		assert self.classroom.update_classRoom(roomName,id)["success"]==True

	 
	@allure.title("删除教室")
	@pytest.mark.run(order=4)
	def test_del(self, data):
		try:
			id = self.classroom.search_classRoom(data[1])["data"][0]["id"]
			assert self.classroom.delete_classRoom(str(id))["success"] == True
		except Exception as e:
			self.log.error(e)
			
		






		

	
	
	