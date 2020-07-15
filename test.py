# x = ["Joe", "2", "Ted", "4.98", "14", "Sam", "void *", "42", "float", "pointers", "5006"]

# for element in x:
#     print(element)


y = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

# for element in y:
#     print(element)
def nested_print(arr):
    for elem in arr:
        if type(elem) == list:
            nested_print(elem)
        else:
            print(elem)


nested_print(y)
    