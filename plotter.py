import plotly.graph_objects as go
from datetime import datetime as dt


def plotppl(person_data, sums_update=False, timestamps=None):
    ppl = []
    differmsg = []
    pplmsg = []
    memsg = []
    summsg = []
    frequency = []

    for pers in person_data:

        if not sums_update:
            you_msg = list(person_data[pers]['msg_count'].values())[0]
            me_msg = list(person_data[pers]['msg_count'].values())[1]

        else:
            you_msg_all = list(person_data[pers]['msgs'].values())[0]
            me_msg_all = list(person_data[pers]['msgs'].values())[1]
            try:
                you_msg = len(list(filter(lambda x: timestamps[1] > x[1]/1000 > timestamps[0],you_msg_all)))
                me_msg = len(list(
                    filter(lambda x: timestamps[1] > x[1]/1000 > timestamps[0],
                       me_msg_all)))

            except TypeError as e:
                print(e)
                print(you_msg_all)
                print(you_msg)


        if you_msg + me_msg > 100:
            ppl.append(pers.replace("_", " "))
            summsg.append(me_msg + you_msg)
            pplmsg.append(you_msg)
            memsg.append(me_msg)
            if not sums_update:
                differmsg.append(me_msg - you_msg)
                frequency.append(person_data[pers]['frequency'])

        else:
            continue

    if not sums_update:
        return differ(ppl, differmsg), sums(ppl, summsg, pplmsg, memsg), freq(ppl, frequency)

    else:
        try:
            return sums(ppl, summsg, pplmsg, memsg)
        except ValueError as e:
            print(e)
            print(ppl)
            print(summsg)
            print(pplmsg)
            print(memsg)


def differ(ppl, dif):
    all = list(zip(ppl, dif))
    all.sort(key=lambda tup: tup[1])
    ppl1, differmsg1 = zip(*all)
    fig1 = go.FigureWidget(data=[go.Bar(x=ppl1, y=differmsg1)])
    fig1.update_layout(title="Message count difference -> me - you")

    return fig1


def sums(ppl, summsg, pplmsg, memsg):

    all = list(zip(ppl, summsg, pplmsg, memsg))
    all.sort(key=lambda tup: tup[1])
    ppl2, summsg2, pplmsg2, memsg2 = zip(*all)
    fig2 = go.FigureWidget(data=[
        go.Bar(name='You', x=ppl2, y=pplmsg2, hoverinfo='y+text', hovertext=ppl2),
        go.Bar(name='Me', x=ppl2, y=memsg2, text=summsg2, texttemplate='%{text:.2s}', textposition='outside',
               hoverinfo='y+text', hovertext='Me')

    ])
    fig2.update_layout(title='Message count by user', barmode='stack', height=600)

    return fig2


def freq(ppl, frequency):
    all = list(zip(ppl, frequency))
    all.sort(key=lambda tup: tup[1])
    ppl3, frequency1 = zip(*all)
    fig3 = go.FigureWidget(data=[go.Bar(x=ppl3, y=frequency1)])
    fig3.update_layout(title="Message frequency -> messages per day")

    return fig3
