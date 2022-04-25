

import discord
import time
 
client = discord.Client()
 
# チャンネル入退室時の通知処理
@client.event
async def on_voice_state_update(member, before, after):
 
    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if before.channel != after.channel:
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel(949091439969697814)
 
        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        announceChannelIds = [842449150321885188, 946120184333221958, 946120235193356308]
 
        # 入室通知
        if after.channel is not None and after.channel.id in announceChannelIds:
            
            if leave_name == member.name:
                t = time.time - start

                if t < 5:
                    return
            

            
            await botRoom.send("**" + after.channel.name + "** に、__" + member.name + "__  が入室しました")

        #退室
        if before.channel is not None and before.channel.id in announceChannelIds:
            leave_name = member.name
            start = time.time()


 
# Botのトークンを指定
client.run()



 start = time.time()
 t = time.time - start

 if t < 5:
