def comparison_num(in_list):
    a = len(set(in_list))
    if a == len(in_list):
        return 0
    else:
        return len(input_list) - a + 1


i = 0
input_list = []
while i != 3:
    input_list.append(int(input()))
    i += 1
print(comparison_num(input_list))
