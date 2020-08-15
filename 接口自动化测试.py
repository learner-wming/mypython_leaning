import requests
import json
url = "http://47.241.12.65:8080/login"
para = {"usetname":"admin1",
        "password":"111111"
}

res = requests.get(url,para)
print(res)
# print(res.text)
# print(res.content)
con = json.loads(res.text)
print(con)

#到目前为止（2020-08-16 2：45） 我安装了 pyMysql requests  xrld三个第三方库
#