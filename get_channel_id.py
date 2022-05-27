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

    def rece_textch(self):
        return int(self.channels["voicechannel_notice"])


client = discord.Client()
ch = Channel()


@client.event
async def on_ready():
    for channel in client.get_all_channels():
        
        ch.receive_channels(channel.name,channel.id)


client.run(get_token.get_token())
