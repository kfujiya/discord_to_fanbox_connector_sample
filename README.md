# discord to fanbox connector

## 1. 概要
承認制discordサーバについて、参加者の自動制御を行うアプリケーションです。  
知人の依頼をもとに構築中のものになります。  
元ネタはゆきみしのさんのアイデアです: https://note.com/fujii_shino/n/n5f1d6f057db4

## 2. 必要なもの
* python 3.9以上
  - https://www.python.jp/install/windows/install.html
  - https://qiita.com/shun_sakamoto/items/7944d0ac4d30edf91fde
* pythonライブラリ(仮想環境にインストールするとよい)
  - Helium
  - requests
  - discord.py

* pixiv FANBOXアカウント
  - ユーザ名, パスワード

* discordサーバ
  - サーバID
  - discordアプリケーションのクライアントID, シークレットコード, アプリケーションコード( https://apidog.com/jp/blog/discord-api/ )

## 3. 作業内容
* このリポジトリをクローンする
* pixiv FANBOXアカウントとdiscordの情報をsecret.iniに書き込む
* コマンドでコネクターを実行する
  - `\.venv\Scripts\activate`
  - `python pixivConnectorBatch.py`

* bot形式で実行し続ける(サーバーにbotを登録してあり、かつsecret.iniにbotを呼び出すtokenを記載する必要あり)
  - `\.venv\Scripts\activate`
  - `python pixivConnectorBot.py`
