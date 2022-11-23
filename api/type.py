# -*- coding:utf-8 -*-
"""
@Time:2022/11/21 9:56 上午
@Auth:amanda
@Function:课后服务类型接口
"""
from util.baseApi import baseApi


class class_Type(baseApi):
	def search_type(self, name):
		data = {
			"method": "post",
			"url": "https://" + self.set_url() + "/web/api/v1/type/page",
			"headers": {
				"Access-Token": self.token,
				"user-agent": "3333"
				
			},
			"json": {
				"name": name,
				"schoolId": self.schoolId,
				"current": 1,
				"size": 10
			}
		}
		return self.send(data)
	
	#新增类型
	def save_type(self,name,source):
		data = {
			"method": "post",
			"url": "https://" + self.set_url() + "/web/api/v1/type/save",
			"headers": {
				"Access-Token": self.token,
				"user-agent": "3333"
			},
			"json": {
				"name": name,
				"schoolId": self.schoolId,
				"source":source,
				"createId": self.id
			}
		}
		
		return self.send(data)
		
	#修改类型
	def update_type(self,name,source,id):
			data = {
				"method": "post",
				"url": "https://" + self.set_url() + "/web/api/v1/type/update",
				"headers": {
					"Access-Token": self.token,
					"user-agent": "3333"
				},
				"json": {
					"name": name,
					"schoolId": self.schoolId,
					"source":source,
					"id": id,
					"updateId":self.id
				}
			}
			return self.send(data)
	
	#删除类型
	def delete_type(self,id):
			data = {
				"method": "get",
				"url": "https://" + self.set_url() + "/web/api/v1/type/delete?ids=" + id,
				"headers": {
					"Access-Token": self.token,
					"user-agent": "3333"
				}
			}
			return self.send(data)