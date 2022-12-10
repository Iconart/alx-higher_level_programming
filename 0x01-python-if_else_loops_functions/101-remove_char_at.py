#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return(str)
    else:
        i = 0
        new_sentence = ""
        while i < len(str):
            if str[i] != str[n]:
                new_sentence += str[i]
            i += 1
        return(new_sentence)
