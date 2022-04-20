def splitText_noRepeat(input_text):
    input_text = input_text.lower()
    split_text = input_text.split(" ")
    output_list = []
    for split_text in split_text:
        if split_text not in output_list:
            output_list.append(split_text)
    return output_list


if __name__ == '__main__':
    input_fullText = input()
    output_list = splitText_noRepeat(input_fullText)
    output_len = len(output_list)
    for i, output_word in enumerate(output_list):
        if i == output_len - 1:
            print(output_word)
        else:
            print(output_word, end=" ")