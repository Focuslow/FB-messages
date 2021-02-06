import json
from Person import Person
from datetime import datetime


def get_data(path):
    with open(path) as json_file:
        data = json.load(json_file)

    if (len(data['participants'])) > 2 or (len(data['participants'])) == 1:
        return 0

    weird_name = (data['participants'][:])
    fixed_names = []
    person_dict = {}
    min_time = 1679326888341
    max_time = 0
    for c, i in enumerate(weird_name):
        name = i['name']
        name_fix = name.encode('latin1').decode('utf8')
        fixed_names.append(name_fix)
        c = Person(name_fix)
        d = {name_fix: c}
        person_dict.update(d)

    person_dict.update({'names': fixed_names})
    for event in data['messages']:
        msg_time = event["timestamp_ms"]
        if msg_time < min_time:
            min_time = msg_time
        if msg_time > max_time:
            max_time = msg_time

        sender_bad = event['sender_name']
        sender_str = sender_bad.encode('latin1').decode('utf8')
        if sender_str not in person_dict['names']:
            return 0

        time = event['timestamp_ms']
        try:
            test = datetime.fromtimestamp(time)
            time = time /1000
        except OSError:
            pass
        sender = person_dict[sender_str]
        if 'content' in event.keys() and 'call_duration' not in event.keys():
            msg = event['content']
            if msg != "You can now call each other and see information such as Active Status and when you've read messages." and msg != "You are now connected on Messenger.":
                decoded_msg = msg.encode('latin1').decode('utf8')
                sender.msgs.append([decoded_msg, time])
                sender.msg_count += 1
                sender.msg_length += len(decoded_msg)

        elif 'sticker' in event.keys():
            sender.stickers.append(time)

        elif 'photos' in event.keys():
            sender.photos.append(time)

        elif 'videos' in event.keys():
            sender.videos.append(time)

        elif 'gifs' in event.keys():
            sender.gifs.append(time)

        elif 'files' in event.keys():
            sender.files.append(time)

        elif 'audio_files' in event.keys():
            sender.audio_files.append(time)

        if 'call_duration' in event.keys() and event['call_duration'] != 0:
            sender.calls.append(time)
            sender.call_durations += event['call_duration']

    if sender.msg_count > 50:
        list(person_dict.values())[0].time = [min_time, max_time]
        list(person_dict.values())[1].time = [min_time, max_time]
        list(person_dict.values())[0].frequency = sender.msg_count / ((max_time - min_time) / 86400000)
        list(person_dict.values())[1].frequency = sender.msg_count / ((max_time - min_time) / 86400000)
    # if list(person_dict.values())[0].msgs:
    #     print(list(person_dict.values())[0].name)
    #     print(list(person_dict.values())[0].msgs[-1])
    return person_dict
