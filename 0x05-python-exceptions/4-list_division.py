#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    div_result = 0
    for i in range(list_length):
        try:
            div_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            div_result = 0
            print("division by 0")
        except (ValueError, TypeError):
            div_result = 0
            print("wrong type")
        except IndexError:
            div_result = 0
            print("out of range")
        finally:
            new_list.append(div_result)
    return new_list
