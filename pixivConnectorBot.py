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
hello_command  = re.compile(r'^!hello')
getRoleMembers_command = re.compile(r'^!getRoleMembers.*')

# サーバー情報を取得する
def getGuild():
    return client.get_guild(applicationSetting.get("discord", "guild_id"))

def getRoleMembers(guild, role_id):
    # 特定のロールIDのロールオブジェクトを取得する
    role = guild.get_role(role_id)

    # ロールオブジェクトのメンバーを取得する
    members = role.members
    return members

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

    # メッセージが!helloで始まる場合, helloと返す
    if hello_command.match(message.content):
        await message.channel.send('Hello!')

    # メッセージが!getRoleMembersで始まる場合, そのあとに入力したロールのメンバを取得する
    if getRoleMembers_command.match(message.content):
        checkFlg = False

        # コメントのサーバ情報
        guild = message.guild
        if guild == None:
            print("サーバ情報が取得できませんでした")
            return

        guildRoles = guild.roles

        searchRoleName = message.content.split()[1]
        print("検索対象ロール: " + searchRoleName)
        for gRole in guildRoles:
            print("確認ロール: " + gRole.name)
            if gRole.name == searchRoleName:
                memberList = getRoleMembers(guild, gRole.id)
                memberNameList = []
                for member in memberList:
                    memberNameList.append(member.name)
                await message.channel.send("メンバーは次の通りです。\n" + ', '.join(memberNameList))
                print("メンバーは次の通りです。\n" + ', '.join(memberNameList))
                checkFlg = True
                break

        if checkFlg == False:
            await message.channel.send("ロールが見つかりませんでした!")
            print("ロールが見つかりませんでした!")

# discord botを動かす場合
client.run(discordToken)