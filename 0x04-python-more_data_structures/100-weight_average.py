#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    score_list = [t[0] for t in my_list]
    weight_list = [t[1] for t in my_list]
    score_times_weight_list = []
    for x, y in zip(score_list, weight_list):
        score_times_weight_list.append(x * y)
    return sum(score_times_weight_list) / sum(weight_list)
