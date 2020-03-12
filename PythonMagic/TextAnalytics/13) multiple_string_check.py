def multiple_string_check(text):
    count = 0
    string1 = "finance"
    string2 = "analytics"
    word_count1 = text.count(string1)
    word_count2 = text.count(string2)
    if word_count1 >= 1 and word_count2 >= 1:
        count = 1
    return count

text = "finance is a major field of application for python. in finance  are key."

print(text)
print(multiple_string_check(text))

