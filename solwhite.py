import requests
import time

invite_url = 'https://www.gookaito.com/ref?link=Z14ecFt'
wallet_url = 'https://www.gookaito.com/api/wallets'

# 读取地址
with open('soladdress.txt', 'r') as file:
    wallet_list = [line.strip() for line in file if line.strip()]

for wallet in wallet_list:
    session = requests.Session()

    # Step 1: 访问邀请链接（设置 Cookie）
    session.get(invite_url, headers={
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'https://www.gookaito.com/',
    })

    # Step 2: 提交钱包
    data = {
        'wallet': wallet
    }

    headers = {
        'Content-Type': 'application/json',
        'Origin': 'https://www.gookaito.com',
        'Referer': invite_url,
        'User-Agent': 'Mozilla/5.0',
    }

    response = session.post(wallet_url, json=data, headers=headers)

    print(f"[{wallet}] 状态码: {response.status_code} 响应: {response.text}")

    # 可选：每次间隔 1 秒，防止过快请求被封
    time.sleep(1)
