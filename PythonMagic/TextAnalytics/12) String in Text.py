def string_check(text):
    count = 0
    string = "finance"
    word_count = text.count(string)
    if word_count >= 1:
            count = 1
    return count


text = "finance is a major filed of application for python. in finance analytics are key."

print(text)
print(string_check(text))

