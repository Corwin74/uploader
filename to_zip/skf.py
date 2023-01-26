input_num = '123'

def f1(num_str, buff):
    global result_list
    buff_loc = buff
    if len(num_str) == 0:
        if len(buff_loc) > len(result_list):
            result_list = buff_loc
    else:
        for i in range(len(num_str)):
            num = num_str[:i+1]
            if num_str[i+1:i+2] == '0':
                continue            
            if num not in buff_loc:
                buff_loc.append(num)
                #print('buff_list:', num, num_str[i+1:], buff_loc)
                f1(num_str[i+1:], buff_loc)
    return


buff=[]
result_list=[]
f1(input_num, buff)
print(result_list)