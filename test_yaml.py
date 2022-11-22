# -*- coding:utf-8 -*-
"""
@Time:2022/11/17 3:48 下午
@Auth:amanda
@Function:自动生成yaml文件
"""

import yaml


def yaml():
 	env = {
 		"defult": "test",
 		"ksedu":
 			{
 			"dev": "",
 			"test": "10.2.128.204:8081"
 			}
 		  }
	with open("env2.yaml", "w") as f:
 		yaml.safe_dump(data=env, stream=f)



