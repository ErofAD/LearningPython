'''Найти самую длинную последовательность,
упорядоченную по возрастанию [1, 3, 5, 2, 3, 8, 10, 9, 6, 5, 7, 9, 0]'''
'''def sequenceSearch (my_list, iter, num=0, sum=0):
    if iter == 0:
        sequenceSearch(my_list, iter+1)
    elif iter == len(my_list):
        if my_list[iter]>my_list[iter-1]:
            
'''
def num3():
    my_list = [1, 3, 5, 2, 3, 8, 10, 9, 4, 5, 7, 9, 10]
    #my_list = [1, 2, 3]
    sum_max = 0
    num = 0
    s = 1
    for i in range(1, len(my_list)):
        if my_list[i] > my_list[i-1]:
            s += 1
            if i == len(my_list) - 1 and sum_max < s:
                sum_max = s
                num = i - sum_max + 1
        else:
            if sum_max < s:
                sum_max = s
                num = i-sum_max
            s = 1

    return (my_list[num:num+sum_max])



