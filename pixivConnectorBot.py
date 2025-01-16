import discord
import json
import configparser
import re

## ファイルからFANBOX, Discordの鍵情報を取得する
applicationSetting = configparser.ConfigParser()
applicationSetting.read('secret.ini', encoding='utf-8')

## discord setting
discordAuthClientID = applicationSetting.get("discord", "client_id")
discordAuthSecretID = applicationSetting.get("discord", "secret_id")
discordAuthCode     = applicationSetting.get("discord", "OAuthCode")
discordToken        = applicationSetting.get("discord", "token")

# discordクライアント作成
client = discord.Client(intents=discord.Intents.all())

# コマンド接頭辞の正規表現設定
command_prefix = re.compile(r'^!')
getRoleMembers_command = re.compile(r'^!getRoleMembers$')
setClientRole_command = re.compile(r'^!setClientRole$')

# サーバーに参加しているメンバー一覧を取得する
def getGuildMembers(guild):
    members = guild.members
    return members

# ロールに所属するメンバーを取得する
def getRoleMembers(guild, role_id):
    # 特定のロールIDのロールオブジェクトを取得する
    role = guild.get_role(role_id)

    # ロールオブジェクトのメンバーを取得する
    members = role.members
    return members

# ユーザにロールを追加する
def joinRole(guild, role_id, user_name):
    # ロールIDからオブジェクトを取得する
    role = guild.get_role(role_id)

    # ユーザ名からオブジェクトを取得してロール追加する
    user = guild.get_member_named(user_name)
    await user.add_roles(role, "自動追加処理")

# ロールごとのメンバー一覧を取得
def getMembers():
    # botのいるサーバ情報を取得する
    guild = client.guild
    if guild == None:
        print("サーバ情報が取得できませんでした")
        return

    # ロール一覧, ユーザ辞書
    guildRoles = guild.roles
    roleMemberList = {}

    # ロールごとに
    for gRole in guildRoles:

        # for debug
        print("確認ロール: " + gRole.name)

        # メンバー情報を取得して辞書に格納する
        memberList = getRoleMembers(guild, gRole.id)
        if len(memberList) > 0:
            roleMemberList[gRole.name] = memberList

    return roleMemberList


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('on_ready!')

@client.event
async def on_message(message):
    print('message recieved')

    # メッセージがbotからのものであれば無視する
    if message.author.bot:
        return

    # for debug
    print(message.content)

    # メッセージがコマンド接頭辞を含まない場合は無視する
    if not command_prefix.match(message.content):
        return

    # メッセージが!getRoleMembersの場合, 各ロールのメンバー名を取得する
    if getRoleMembers_command.match(message.content):
        roleMemberList = getMembers()

        # for debug
        for role in roleMemberList.keys():
            members = roleMemberList[role]
            memberNames = [member.name for member in members]
            await message.channel.send(role + "のメンバー: " + ', '.join(memberNames))

    # メッセージが!setClientRoleの場合, pixiv FANBOXの支援者情報を確認してロールを追加する
    if setClientRole_command.match(message.content):
        print("this command under construction")

# discord botを動かす
client.run(discordToken)