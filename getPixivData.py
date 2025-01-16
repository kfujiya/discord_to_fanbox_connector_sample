from helium import *
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

# pixiv FANBOXのファン一覧を取得する
def getSupporters():
    # ファンリストリストを作成する
    fanListDict = {}

    # FireFoxを開いてpixivのログインページを開く
    start_firefox("https://accounts.pixiv.net/login?prompt=select_account&return_to=https%3A%2F%2Fwww.fanbox.cc%2Fauth%2Fstart&source=fanbox")

    # intoで指定した要素に文字列を入力する
    write(pixivUser, into='メールアドレスまたはpixiv ID')
    write(pixivPass, into='パスワード')

    # ログインをクリックして指定ページまで移動
    click("ログイン")
    # for debug(メールを見てpixivのニ要素認証を処理したい)
    wait_until(helium.Text("ファン一覧").exists, 120, 5)
    click("ファン一覧")

    # プラン名ごとにファン一覧を取得する
    for plan in applicationSetting.get("fanbox_plan", "plans"):
        wait_until(helium.Text(plan).exists)
        click(plan)
        time.sleep(5)

        planFanList = []
        # 各ページごとにファン一覧を追加
        while True:
            # ファン一覧を取得
            fans = find_all(S("#supporter-list-item"))
            for fan in fans:
                fanName = fan.web_element.text
                planFanList.append(fanName)

            # 次のページがあるか確認
            if S(".btn-next").exists():
                click(S(".btn-next"))
                time.sleep(5)
            else:
                break

        fanListDict[plan] = planFanList


    # ブラウザを閉じる
    kill_browser()

    return fanListDict

supporters = getSupporters()

# ファンリストを表示
for plan in supporters:
    print(plan + " : ")
    for supporter in supporters[plan]:
        print(supporter)
    print("\n")