import plotly.express as px
import pandas as pd
import numpy as np


def graph(words_me, words_you, person):
    my_words = list(words_me.keys())
    your_words = list(words_you.keys())
    my_words_count = sum(list(words_me.values()))
    your_words_count = sum(list(words_you.values()))
    me_occur = words_me
    you_occur = words_you
    old_x = []
    y = []
    x = []
    me = []
    you = []
    labels = []
    word_occurence = {}

    for word in my_words:
        word_occurence[word] = words_me[word]
        if word not in list(words_you.keys()):
            words_you[word] = 0
    for word in your_words:
        if word not in list(words_me.keys()):
            word_occurence[word] = words_you[word]
            words_me[word] = 0
            x.append(-(words_you[word]) / word_occurence[word])

        else:
            word_occurence[word] += words_you[word]
            if (words_me[word] - words_you[word]) == 0:
                x.append(0)
            elif (words_me[word] - words_you[word]) > 0:
                x.append((words_me[word] - words_you[word]) / word_occurence[word])
            elif (words_me[word] - words_you[word]) < 0:
                x.append((words_me[word] - words_you[word]) / word_occurence[word])

        y.append((np.exp(word_occurence[word] / 10000)))
        # y.append((np.log(word_occurence[word]))) weird exp functions
        labels.append(word)
        you.append(words_you[word])
        me.append(words_me[word])

    df = pd.DataFrame(dict(X=x, Y=y, Labels=labels, You=you, Me=me))
    trace = px.scatter(df, x='X', y='Y', hover_name='Labels',
                       hover_data={'X': False, 'Y': False, 'You': ':.0f', 'Me': ':.0f'})
    trace.update_layout(title="Word occurence for " + person, xaxis_title="Me", yaxis_title="You")
    return trace

    # fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers', hovertemplate="<b>%{text}</b><br><br>" +
    #                                                                         "Me: %{me:.0f}<br>" +
    #                                                                         "You: %{you:.0f}<br>" +
    #                                                                         "<extra></extra>", text=labels, me=me, you=you))
    # fig.show()
