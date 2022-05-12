# def sortDigitAndSort(numbers):
#     digit_sums = []  # 紀錄每個位數的加總

#     # 將總每個位數，append到digit_sums
#     for number in numbers:
#         digit_sum = 0
#         for digit in number:
#             digit_sum += int(digit)
#         digit_sums.append(digit_sum)

#     # 把digit_sums每個元素的索引記錄起來
#     index_digitSum_pairs = [[i, digit_sum]
#                             for i, digit_sum in enumerate(digit_sums)]
#     # 利用每個位數總和(p[1])與原本的數字大小(numbers[p[0]])對index_digitSum_pairs做排序
#     # 依照十進位中各位數字和由小到大排序輸出。如果各位數字和相等則比較數值由小到大排列
#     sorted_pairs = sorted(index_digitSum_pairs,
#                           key=lambda p: (p[1], int(numbers[p[0]])))
#     # 利用記錄在sorted_pairs內的索引取得numbers內對應位置的元素
#     sorted_numbers = [numbers[i] for i, digitSum in sorted_pairs]
#     return sorted_numbers


# if __name__ == '__main__':
#     input_amount = int(input())
#     input_numbers_str = input()
#     input_numbers = input_numbers_str.split()
#     sorted_numbers = sortDigitAndSort(input_numbers)
#     output = " ".join(sorted_numbers)
#     print(output)

num=int(input())
N=[0]*num
M=[0]*num
N=input().split()
total=0
for i in range(0,num,1):
    for o in range(0,len(N[i]),1):
        total=total+int(N[i][o])
    M[i]=total
    total=0
for i in range(0,num,1):
    for o in range(i+1,num,1):
        if M[i]>M[o]:
            change=M[o]
            M[o]=M[i]
            M[i]=change
            change=N[o]
            N[o]=N[i]
            N[i]=change
        if M[i]==M[o]:
            if N[i]>N[o]:
                change=M[o]
                M[o]=M[i]
                M[i]=change
                change=N[o]
                N[o]=N[i]
                N[i]=change
for i in range(0,num):
    if i<num-1:
        print(N[i],end=' ')
    else:
        print(N[i])
