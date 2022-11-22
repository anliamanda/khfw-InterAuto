# -*- coding:utf-8 -*-
"""
@Time:2022/11/17 2:19 下午
@Auth:amanda
@Function:教室信息接口
"""

from util.baseApi import baseApi



class class_Room(baseApi):
	#查询教室
	def search_classRoom(self,roomName):
		data = {
			"method": "post",
			"url": "http://"+self.set_url()+"/web/api/v1/classRoom/list",
			"headers":{
				"Access-Token":self.token
				
			},
			"json": {
				"roomName":roomName,
				"schoolId":self.schoolId
		}
		}
		return self.send(data)
	
	#教室信息新增
	def save_classRoom(self,roomName):
		data = {
			"method": "post",
			"url": "http://" + self.set_url() + "/web/api/v1/classRoom/save",
			"headers": {
				"Access-Token": self.token
			},
			"json": {
				"roomName": roomName,
				"schoolId": self.schoolId,
				"createId": self.id
			}
		}
		return self.send(data)


	#教室信息修改
	def update_classRoom(self,roomName,id):
		data = {
			"method": "post",
			"url": "http://" + self.set_url() + "/web/api/v1/classRoom/update",
			"headers": {
				"Access-Token": self.token
			},
			"json": {
				"roomName": roomName,
				"schoolId": self.schoolId,
				"id":id
			}
		}
		return self.send(data)
	
	#教室信息删除
	def delete_classRoom(self,id):
		data = {
			"method": "get",
			"url": "http://" + self.set_url() + "/web/api/v1/classRoom/del?id="+id,
			"headers": {
				"Access-Token": self.token
			}
		}
		return self.send(data)