# Notice_bot.py
 
import discord
 
client = discord.Client()
 
# 起動時処理
@client.event
async def on_ready():
    for channel in client.get_all_channels():
        print("----------")
        print("チャンネル名：" + str(channel.name))
        print("チャンネルID：" + str(channel.id))
        print("----------")
 
# Botのトークンを指定（デベロッパーサイトで確認可能）
client.run('OTQ5MDg0MTE0NTM4MDkwNTM4.YiFNdg.IJJYOxNjyMw4H3FeHmcp9tvGNWk')