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
		data=yaml.safe_load(open("./config/login.yaml"))
		return self.send(data)
	
	def get_userinfo(self):
		self.token = self.userinfo()["data"]["token"]
		self.schoolId = self.userinfo()["data"]["schoolId"]
		self.id = self.userinfo()["data"]["id"]
		data = {
			"token": self.token,
			"schoolId": self.schoolId,
			"id": self.id
		}
		if not os.path.exists("./config/userinfo.yaml"):
			with open("./config/userinfo.yaml", "w") as f:
				yaml.safe_dump(data=data, stream=f)
		else:
			with open("./config/userinfo.yaml", "r") as f:
				data = yaml.load(f,Loader=yaml.FullLoader)
		return data
