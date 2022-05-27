class Channel:

    channel_name = []
    channel_id = []

    def __init__(self):
        pass

    def receive_name(self, name):
        self.channel_name.append(name)

    def receive_id(self, id):
        self.channel_id.append(id)

    def print_list(self):
        print(self.channel_name, self.channel_id)

c = Channel()

#Text Channels 966831928609243208
#Voice Channels 966831928609243209
#text_1 966831929058025482
#voice_1 966831929058025483
#text_2 966932818020155423
#voice_2 966932993484656680