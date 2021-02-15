def reverseWordsInString(string):
    final_string = ''

    i = len(string) - 1
    current_word_end = i

    while i >= 0:

        while i >= 0 and (string[i]) != ' ':
            i -= 1
        final_string += string[i + 1:current_word_end+1]

        while i >= 0 and string[i] == ' ':
            i -= 1
            final_string += ' '

        current_word_end = i

    return final_string

