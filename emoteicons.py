
def emoteicons(msg, emoteicon):
    if msg.find(emoteicon) != -1:
        if msg == emoteicon:
            msg = "<img class='emote-big' src='/assets/emote-icons/%s.gif'>" % emoteicon
            return msg
        else:
            msg = msg.replace(emoteicon,
                              "<img class='emote-small' src='/assets/emote-icons/%s.gif'>" % emoteicon)
            return msg
    else:
        return msg


def emoteicon(msg):
    msg = emoteicons(msg, "SmartNinja")
    msg = emoteicons(msg, "DeaD")
    msg = emoteicons(msg, "WinkWink")
    msg = emoteicons(msg, "SumljiV")
    msg = emoteicons(msg, "DeviL")
    msg = emoteicons(msg, "MhehE")
    msg = emoteicons(msg, "RlY")
    msg = emoteicons(msg, "SaD")
    msg = emoteicons(msg, "WooT")
    msg = emoteicons(msg, "ZombiE")

    return msg
