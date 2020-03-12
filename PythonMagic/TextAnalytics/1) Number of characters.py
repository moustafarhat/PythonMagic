def char_count(text): 
    text = text.replace(" ", "")
    return len(text)

word = "finance"
print(char_count(word)) 
