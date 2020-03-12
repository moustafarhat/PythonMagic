def avg_word(text): 
    words = text.split()
    return (sum(len(word) for word in words)/len(words)) 

text = "This is to test the average word length"

print(avg_word(text))
