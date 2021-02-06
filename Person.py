class Person:
    def __init__(self, name):
        self.name = name
        self.call_durations = 0
        self.calls = []
        self.msg_count = 0
        self.msgs = []
        self.msg_length = 0
        self.stickers = []
        self.photos = []
        self.videos = []
        self.gifs = []
        self.files = []
        self.audio_files = []
        self.time=[float('inf'),0]

    def update(self, data):
        self.call_durations += data.call_durations
        self.calls.extend(data.calls)
        self.msg_count += data.msg_count
        self.msgs.extend(data.msgs)
        self.msg_length += data.msg_length
        self.stickers.extend(data.stickers)
        self.photos.extend(data.photos)
        self.videos.extend(data.videos)
        self.gifs.extend(data.gifs)
        self.files.extend(data.files)
        self.audio_files.extend(data.audio_files)

        if data.time[0] < self.time[0]:
            self.time[0] = data.time[0]
        if data.time[1] > self.time[1]:
            self.time[1] = data.time[1]



    def printer(self):
        print('From: ' + str(self.name))
        print('Message count: ' + str(self.msg_count))
        print('Messages overall length: ' + str(self.msg_length))
        if self.call_durations != 0:
            print('Calls: ' + str(len(self.calls)))
            print('Call durations: ' + str(self.call_durations))
        print('Photo count: ' + str(len(self.photos)))
        print('Video count: ' + str(len(self.videos)))
        print('Voice: ' + str(len(self.audio_files)))
        print('Sticker count: ' + str(len(self.stickers)))
        print('Gif count: ' + str(len(self.gifs)))
        print('Files count: ' + str(len(self.files)))
