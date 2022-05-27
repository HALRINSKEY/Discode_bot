import discord
import get_token

class Channel:

    channels = {}

    def __init__(self):
        pass

    def receive_channels(self, name, id):
        self.channels[name] = str(id)

    def print_channels(self):
        for name, id in self.channels.items():
            print("name:" + name + " id:" + id)


client = discord.Client()
c = Channel()


@client.event
async def on_ready():
    for channel in client.get_all_channels():
        
        c.receive_channels(channel.name,channel.id)

    c.print_channels()    

client.run(get_token.get_token())

#Text Channels 966831928609243208
#Voice Channels 966831928609243209
#text_1 966831929058025482
#voice_1 966831929058025483
#text_2 966932818020155423
#voice_2 966932993484656680
 