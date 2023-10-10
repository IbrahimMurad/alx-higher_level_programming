my_dict = {'name': "Ahmed", 'age': 35, 'height': 170, 'male': True}
sub = {key: val for key, val in my_dict.items() if key in ['name', 'male']}
print(sub)