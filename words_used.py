import unicodedata as ud
import unidecode
from count_msgs import count


def words_used(exchange, name, timedown=0, timeup=0):
    words_me = {}
    words_you = {}
    msgs_me = exchange['msgs'][name]
    msgs_you = exchange['msgs'][str(list(exchange['msgs'].keys())[0])]

    msgs_me = limit_time(msgs_me, timedown, timeup)
    msgs_you = limit_time(msgs_you, timedown, timeup)

    words_me = count(msgs_me)
    words_you = count(msgs_you)

    return words_me, words_you


def limit_time(msgs, timedown, timeup):
    out = []
    for k in msgs:
        if timedown == 0 and timeup == 0:
            out.append(k[0])

        elif timedown == 0 and timeup !=0:
            if k[1] <= timeup:
                out.append(k[0])

        elif timeup == 0 and timedown !=0:
            if k[1] >= timedown:
                out.append(k[0])

        elif k[1] <= timeup and k[1] >= timedown:
            out.append(k[0])

    return out