from unidecode import unidecode


def count(msgs):
    out_msgs={}
    for msg in msgs:
        if isinstance(msg[0], list):
            msgs.remove(msg)
            continue
        if isinstance(msg,list):
            msg =  msg[0]
        content = msg.lower()
        words = content.split()
        for word in words:
            if word == ":d":
                word = ":D"
            if word.isalpha():
                if len(word)<2:
                    continue
                word = unidecode(word)
            word = word.strip("\"")
            word = word.strip(",")
            word = word.strip(".")
            word1 = word
            word1 = word1.strip("?")
            if word != word1:
                otaznicky = len(word) - len(word1)
                if "?" in list(out_msgs.keys()):
                    out_msgs["?"] += 1 * otaznicky
                else:
                    out_msgs["?"] = 1 * otaznicky

            if word1 in list(out_msgs.keys()):
                out_msgs[word1] += 1
            elif word1=="":
                continue
            else:
                out_msgs[word1] = 1

    return out_msgs
