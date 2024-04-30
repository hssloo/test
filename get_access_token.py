import requests
import json

def get_access_token(app_id, app_secret):
    # 获取 access_token 的接口 URL
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={app_secret}"
    
    # 发送请求
    response = requests.get(url)
    
    # 解析返回的 JSON 数据
    data = response.json()
    
    # 检查响应数据是否有 access_token
    if 'access_token' in data:
        access_token = data['access_token']
        expires_in = data['expires_in']
        print(f"Access Token: {access_token}")
        print(f"Expires In: {expires_in} seconds")
        return access_token
    else:
        print("Failed to get access_token:", data)
        return None

if __name__ == "__main__":
    # 请替换为你的 app_id 和 app_secret
    app_id = "wxb0cdaf534ca78b88"
    app_secret = "726ff7ab457e6f798bfce94a5aa87f32"
    
    # 获取 access_token
    access_token = get_access_token(app_id, app_secret)
