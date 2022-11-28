from tracemalloc import start
import discord
import time
import get_token
 
client = discord.Client()

leave_name = 0
leave_time = 0
 
# チャンネル入退室時の通知処理
@client.event
async def on_voice_state_update(member, before, after):

    global leave_name
    global leave_time

    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if before.channel != after.channel:
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel()
 
        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        announceChannelIds = []
 

        # 入室通知
        if after.channel is not None and after.channel.id in announceChannelIds:
            
            #退室して5秒以内に入室した際は通知しない
            if leave_name == member.name:
                t = time.time() - leave_time

                if t < 5:
                    pass
                else:
                    await botRoom.send(member.name + " entered in " + after.channel.name)
       
            else:
                await botRoom.send(member.name + " entered in " + after.channel.name)
                



        #退室
        if before.channel is not None and before.channel.id in announceChannelIds:
            
            leave_name = member.name
            leave_time = time.time()

client.run(get_token.get_token())


