
changable_list = [1, 2, 3]

def change_list(new_list):
    value_list = changable_list + new_list
    print(value_list)
    for v in value_list:
        print(v)

def sort_lists():
    list = [33, 2.5, 7, 9, 2]
    list.sort(reverse=True)
    print(list)

# change_list(['222', 'helloworld'])
sort_lists()