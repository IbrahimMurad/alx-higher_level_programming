#!/usr/bin/python3
def multiple_returns(sentence):
    sent_len = len(sentence)
    if sent_len == 0:
        return sent_len, "None"
    else:
        return sent_len, sentence[0]
