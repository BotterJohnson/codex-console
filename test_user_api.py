import requests

url = "https://apimail.bigmail.indevs.in/admin/mails"

querystring = {
    "limit":"20",
    "offset":"0",
    # address 为可选参数
    "address":"fphcy82c@bigmail.indevs.in"
}

headers = {
        "x-admin-auth": "Zheng123",
        # "x-custom-auth": "<你的网站密码>", # 如果启用了私有站点密码
    }

response = requests.get(url, headers=headers, params=querystring)

print(response.json())