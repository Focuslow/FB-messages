import plotly.graph_objects as go
from datetime import datetime
from time import mktime
import copy


def get_msgs_time(data_src):
    times = [[], [], []]
    times_you = []
    times_me = []
    data = copy.deepcopy(data_src)
    try:
        for person in data:
            for msg in list(data[person]['msgs'].values())[0]:
                if isinstance(msg[1], list):
                    continue
                timestamp = msg[1] / 1000
                times_you.append(timestamp)

            for msg in list(data[person]['msgs'].values())[1]:
                if isinstance(msg[1], list):
                    continue
                timestamp = msg[1] / 1000
                times_me.append(timestamp)

        times_all = times_me.copy()
        times_all.extend(times_you)
        times_me.sort()
        for i in range(len(times_me)):
            times_me[i] = datetime.fromtimestamp(times_me[i])
        times[1] = times_me
        times_you.sort()
        for i in range(len(times_you)):
            times_you[i] = datetime.fromtimestamp(times_you[i])
        times[2] = times_you
        times_all.sort()
        for i in range(len(times_all)):
            times_all[i] = datetime.fromtimestamp(times_all[i])
        times[0] = times_all
        return times

    except TypeError:
        msgs_info_last = list([])
        msgs_info_first = list([])
        for msg in list(data['msgs'].values())[0].copy():
            if isinstance(msg[1], list) or isinstance(msg[1], str):
                continue
            timestamp = msg[1] / 1000
            times_you.append(timestamp)

        for msg in list(data['msgs'].values())[1].copy():
            if isinstance(msg[1], list) or isinstance(msg[1], str):
                continue
            timestamp = msg[1] / 1000
            times_me.append(timestamp)

        times_all = times_me.copy()
        times_all.extend(times_you)

        times_me.sort()
        for i in range(len(times_me)):
            times_me[i] = datetime.fromtimestamp(times_me[i])
        times[1] = times_me
        times_you.sort()
        for i in range(len(times_you)):
            times_you[i] = datetime.fromtimestamp(times_you[i])
        times[2] = times_you
        times_all.sort()
        for i in range(len(times_all)):
            times_all[i] = datetime.fromtimestamp(times_all[i])
        times[0] = times_all
        msgs_you = list(data['msgs'].values())[0].copy()
        msgs_me = list(data['msgs'].values())[1].copy()
        # last msgs
        try:
            msgs_info_last.append(msgs_you[0])
            msgs_info_last.append(msgs_me[0])
        except IndexError:
            pass

        for msg in msgs_info_last:
            if isinstance(msg[1], list) or isinstance(msg[1], str):
                continue
            else:
                time = int(msg[1] / 1000)
                date1 = datetime.fromtimestamp(time)
                msg[1] = date1.strftime("%d/%b/%Y (%H:%M:%S)")

        # first msgs
        try:
            msgs_info_first.append(msgs_you[-1])
            msgs_info_first.append(msgs_me[-1])
        except IndexError:
            pass

        for msg in msgs_info_first:
            if isinstance(msg[1], list) or isinstance(msg[1], str):
                continue
            else:
                time = int(msg[1] / 1000)
                date1 = datetime.fromtimestamp(time)
                msg[1] = date1.strftime("%d/%b/%Y (%H:%M:%S)")

        msgs_info_first_me_str = ""
        msgs_info_last_me_str = ""
        msgs_info_last_you_str = ""
        msgs_info_first_you_str = ""
        try:
            msgs_info_first_me_str = "Your first message to the person is: " + "\"" + msgs_info_first[1][
                0] + "\"" + " on " + str(msgs_info_first[1][1])
            msgs_info_first_you_str = " Theirs first message to you is: " + "\"" + \
                                      msgs_info_first[0][0] + "\"" + " on " + str(msgs_info_first[0][1])

            msgs_info_last_me_str = "Your last message to the person is: " + "\"" + msgs_info_last[1][
                0] + "\"" + " on " + str(
                msgs_info_last[1][1])

            msgs_info_last_you_str = " Theirs last message to you is: " + "\"" + msgs_info_last[0][
                0] + "\"" + " on " + str(msgs_info_last[0][1])


        except IndexError:
            pass

        return times, msgs_info_first_me_str, msgs_info_last_me_str, msgs_info_last_you_str, msgs_info_first_you_str


def plot_overtime(time_list, type):
    fig1 = go.FigureWidget(data=[go.Scatter(name="All together", x=time_list[0], y=list(range(len(time_list[0]))))])
    fig1.layout.title = 'Message count over time'
    if type == 1:
        trace_name = "Everyone else together"
    if type == 2:
        trace_name = "You"

    fig1.add_scatter(name="Me", x=time_list[1], y=list(range(len(time_list[0]))))
    fig1.add_scatter(name=trace_name, x=time_list[2], y=list(range(len(time_list[0]))))
    fig1.update_layout(hovermode = 'x unified', legend = dict(orientation='h',yanchor='bottom',y=1.02,xanchor='right',x=1))
    return fig1


def time_limiter(year):
    if isinstance(year[0], float) or isinstance(year[1], float):
        month = [int((float(str(i - int(i))) / (1 / 12)).__round__(1)) for i in year]
        year = [int(str(i)[0:4]) for i in year]
        if 0 in month:
            month[month.index(0)] = 1
    else:
        month = [1, 1]
        year = [int(i) for i in year]

    date1 = datetime(year=year[0], month=month[0], day=1)
    date2 = datetime(year=year[1], month=month[1], day=1)

    try:
        timestamp1 = mktime(date1.timetuple())
        timestamp2 = mktime(date2.timetuple())

    except OverflowError as e:
        print(e)
        print(date1)
        print(date2)

    return [timestamp1, timestamp2]
