
 
import discord
 
client = discord.Client()

channel_name = []
channel_id = []
 
# 起動時処理
@client.event
async def on_ready():
    for channel in client.get_all_channels():
        
        channel_name.append(channel.name)
        channel_id.append(channel.id)

    print(channel_name)
    print(channel_id)

# Botのトークンを指定
client.run("OTY2OTMwOTgzOTk3ODI5MjUw.YmI6pw.yLsLeNutdGfR3NaNp_Hy8VFGdqQ")

#966831929058025483 voice 1
#966831929058025482 text 1