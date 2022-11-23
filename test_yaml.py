# -*- coding:utf-8 -*-
"""
@Time:2022/11/17 3:48 下午
@Auth:amanda
@Function:自动生成yaml文件
"""

import yaml


def test_yaml():
	data = {
		"method": "post",
		"url": "https://khfw.ksedu.cn/gateway/web/api/v1/user/login",
		"headers": {
			"user-agent": "3333"
			},
		"json": {
			"userName": "16651687259",
			"password": "5977f8fa67648740112ae69b688261f5"
		}
	}
	with open("config/login.yaml", "w") as f:
 		yaml.safe_dump(data=data, stream=f)

if __name__ == '__main__':
    test_yaml()

