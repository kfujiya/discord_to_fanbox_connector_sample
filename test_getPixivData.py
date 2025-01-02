from helium import *
import discord
import json
import urllib
import requests
import time
import configparser

## ファイルからFANBOX, Discordの鍵情報を取得する
applicationSetting = configparser.ConfigParser()
applicationSetting.read('secret.ini', encoding='utf-8')

## pixiv fanbox
pixivUser = applicationSetting.get("fanbox", "user")
pixivPass = applicationSetting.get("fanbox", "password")

## discord
discordAuthClientID = applicationSetting.get("discord", "client_id")
discordAuthSecretID = applicationSetting.get("discord", "secret_id")
discodeAuthCode     = applicationSetting.get("discord", "OAuthCode")

# discordクライアント作成
client=discord.Client(intents=discord.Intents.all())

# pixiv FANBOXのファン一覧を取得する
def test1():
    # FireFoxを開いてpixivのログインページを開く
    start_firefox("https://accounts.pixiv.net/login?prompt=select_account&return_to=https%3A%2F%2Fwww.fanbox.cc%2Fauth%2Fstart&source=fanbox")

    # intoで指定した要素に文字列を入力する
    write(pixivUser, into='メールアドレスまたはpixiv ID')
    write(pixivPass, into='パスワード')

    # ログインをクリックして指定ページまで移動
    click("ログイン")
    wait_until(helium.Text("ファン一覧").exists)
    click("ファン一覧")
    wait_until(helium.Text("ミニミニ").exists)
    click("ミニミニ")

    # ここどうすればいいか確認する。
    # print(TextFilld("ファン名").value)

    # 10秒撮影用に待つ
    time.sleep(10)

    # ブラウザを閉じる
    kill_browser()

# discord APIを実行する
def test2_discord():

    # アクセスURL/ヘッダー/リクエストデータを設定
    url = 'https://discord.com/api/oauth2/token'

    requestHeader = {
        'Content-Type': 'applicaton/x-www-form-urlencoded'
    }
    requestData = {
        'client_id': discordAuthClientID,
        'client_secret': discordAuthSecretID,
        'grant_type': 'authorization_code',
        'code': discodeAuthCode,
        'redirect_uri': 'http://localhost/discord/redirect'
    }

    requestBody = urllib.parse.urlencode(requestData)

    print(requestBody)

    # リクエストを送信して結果を取得する
    try:
        response = requests.post(url, headers=requestHeader, data=requestBody)
        
        body = response.json().get
        #body = json.loads(response.read())
        headers = response.headers
        status = response.status_code

        print(headers)
        print(body)
        print(status)

    except urllib.error.URLError as e:
        print(e.reason)
        print(e.args)

def test3_discordpy(server_id, role_id):
    # 特定のロールIDのロールオブジェクトを取得する
    ctx = discord.Client(intents=discord.Intents.all())
    guild = ctx.get_guild(server_id)
    role = guild.get_role(role_id)

    # ロールオブジェクトのメンバーを取得する
    members = role.members
    print(members)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('on_ready!')

#test1()
test2_discord()

# discord botを動かす場合
# client.run(token)
