def qwerty(input_string):
    input_string = input_string.lower()
    sequence = "!@#$%^&*()_++`1234567890-=={}||qwertyuiop[]\\:""asdfghjkl;''<>??zxcvbnm,.//  "
    output_string = ""
    for c in input_string:
        c_index = sequence.find(c)
        output_string += sequence[c_index + 1]

    return output_string


if __name__ == '__main__':
    user_input = input()
    output_string = qwerty(user_input)
    print(output_string)