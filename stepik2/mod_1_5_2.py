class Song():
    def __init__(self,artist,song):
        self.artist=artist
        self.song = song
        self.tags = []

    def add_tag(self, *args):
        self.tags.extend(args)

song1 = Song('Киркоров','Зайка моя')
song1.add_tag('rekz', 'здоровья', 'счастья')

print(song1.artist)
print(song1.tags)