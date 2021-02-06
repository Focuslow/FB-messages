class Exchange:
    def __init__(self,Me,You):
        self.name = You.name + ' - Jakub Robota'
        self.call_durations = {You.name:You.call_durations,Me.name:Me.call_durations}
        self.calls = {You.name:You.calls,Me.name:Me.calls}
        self.test = {"0":"haha"}
        self.msg_count = {You.name:You.msg_count,Me.name:Me.msg_count}
        self.msgs={You.name:You.msgs,Me.name:Me.msgs}
        self.msg_length = {You.name:You.msg_length,Me.name:Me.msg_length}
        self.stickers = {You.name:You.stickers,Me.name:Me.stickers}
        self.photos = {You.name:You.photos,Me.name:Me.photos}
        self.videos = {You.name:You.videos,Me.name:Me.videos}
        self.gifs = {You.name:You.gifs,Me.name:Me.gifs}
        self.files = {You.name:You.files,Me.name:Me.files}
        self.audio_files = {You.name:You.audio_files,Me.name:Me.audio_files}
        self.time = You.time
        if self.time:
            self.frequency = (You.msg_count + Me.msg_count) / ((self.time[1]-self.time[0])/86400000)
        else:
            self.frequency = 0
        self.me = Me
        self.you = You
        self.json_save_file = {}

    def printer(self):
        print('Name: ' + str(self.name))
        print('Message count: ' + str(self.msg_count))
        print('Messages overall length: ' + str(self.msg_length))
        if self.call_durations != 0:
            print('Calls: ' + str(self.calls))
            print('Call durations: ' + str(self.call_durations))
        print('Photo count: ' + str(self.photos))
        print('Video count: ' + str(self.videos))
        print('Voice: ' + str(self.audio_files))
        print('Sticker count: ' + str(self.stickers))
        print('Gif count: ' + str(self.gifs))
        print('Files count: ' + str(self.files))

    def json_save(self):
        self.json_save_file.update({"name":[self.you.name,'Jakub Robota']})
        self.json_save_file.update({"call_durations" : self.call_durations})
        self.json_save_file.update({"calls": self.calls})
        self.json_save_file.update({"msg_count": self.msg_count})
        self.json_save_file.update({"msgs": self.msgs})
        self.json_save_file.update({"msg_length": self.msg_length})
        self.json_save_file.update({"stickers": self.stickers})
        self.json_save_file.update({"photos": self.photos})
        self.json_save_file.update({"videos": self.videos})
        self.json_save_file.update({"gifs": self.gifs})
        self.json_save_file.update({"files": self.files})
        self.json_save_file.update({"audio_files": self.audio_files})
        self.json_save_file.update({"audio_files": self.audio_files})
        self.json_save_file.update({"time": self.time})
        self.json_save_file.update({"frequency": self.frequency})
        return self.json_save_file




