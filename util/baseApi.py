import os

import requests
import yaml

class baseApi:
	def __init__(self):
		self.token = self.get_userinfo()["token"]
		self.id = str(self.get_userinfo()["id"])
		self.schoolId = str(self.get_userinfo()["schoolId"])
	
	def send(self,data):
		return requests.request(**data).json()
		
	def set_url(self):
		if os.path.exists("./config/env.yaml"):
			self.env =yaml.safe_load(open("./config/env.yaml"))
			url=self.env["ksedu"][self.env["default"]]
		return url
	
	def userinfo(self):
		_userName = "16651687259"
		_password = "5977f8fa67648740112ae69b688261f5"
		data = {
			"method": "post",
			"url": "http://10.2.128.204:8081/web/api/v1/user/login",
			"json": {
				"userName": _userName,
				"password": _password
			}
		}
		print("=========")
		return self.send(data)
	
	def write_userinfo(self):
		self.token = self.userinfo()["data"]["token"]
		self.schoolId = self.userinfo()["data"]["schoolId"]
		self.id = self.userinfo()["data"]["id"]
		data = {
			"token": self.token,
			"schoolId": self.schoolId,
			"id": self.id
		}
		with open("./config/userinfo.yaml", "w") as f:
			yaml.safe_dump(data=data, stream=f)
			
	def get_userinfo(self):
		if os.path.exists("./config/userinfo.yaml"):
			with open("./config/userinfo.yaml", "r") as f:
				data = yaml.load(f,Loader=yaml.FullLoader)
		else:
			self.write_userinfo()
			with open("./config/userinfo.yaml", "r") as f:
				data = yaml.load(f,Loader=yaml.FullLoader)
		return data

