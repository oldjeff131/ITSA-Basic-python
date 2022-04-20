enum = [
    [
        '*****',
        '*   *',
        '*   *',
        '*   *',
        '*****',
    ],
    [
        '    *',
        '    *',
        '    *',
        '    *',
        '    *',
    ],
    [
        '*****',
        '    *',
        '*****',
        '*    ',
        '*****',
    ],
    [
        '*****',
        '    *',
        '*****',
        '    *',
        '*****',
    ],
    [
        '*   *',
        '*   *',
        '*****',
        '    *',
        '    *',
    ],
    [
        '*****',
        '*    ',
        '*****',
        '    *',
        '*****',
    ],
    [
        '*    ',
        '*    ',
        '*****',
        '*   *',
        '*****',
    ],
    [
        '*****',
        '    *',
        '    *',
        '    *',
        '    *',
    ],
    [
        '*****',
        '*   *',
        '*****',
        '*   *',
        '*****',
    ],
    [
        '*****',
        '*   *',
        '*****',
        '    *',
        '    *',
    ]

]

def numcat(num1:list, num2:list):               #陣列連接
    output = list()
    for i in range(len(num1)):
        output.append(num1[i] + ' ' + num2[i])  #用一個空格隔開
    return output

_input = [int(_) for _ in input()]              #輸入數字

result = enum[_input.pop(0)]                    
for num in _input:
    result = numcat(result, enum[num])

print('\n'.join(result))