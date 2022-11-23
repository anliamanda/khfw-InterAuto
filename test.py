# -*- coding:utf-8 -*-
"""
@Time:2022/11/23 9:59 上午
@Auth:amanda
@Function:请输入模块功能描述
"""
import requests

url="http://khfw.ksedu.cn/gateway/web/api/v1/user/login"
headers={
	"user-agent":"333"
}
data={
	"userName":"16651687259",
	"password":"5977f8fa67648740112ae69b688261f5"
}
r=requests.post(url=url,json=data,headers=headers)
print(r)

