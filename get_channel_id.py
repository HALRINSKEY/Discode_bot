from async_timeout import asyncio
import discord
import channel_id
import get_token

client = discord.Client()
c = channel_id.Channel()

name = []
id = []

@client.event
async def on_ready():
    for channel in client.get_all_channels():
        
        name.append(channel.name)
        id.append(channel.id)
        #c.receive_name(channel.name)
        #c.receive_id(channel.id)
    


    

client.run(get_token.get_token())
#name_c = asyncio(on_ready())
#c.print_list()
print(name)
