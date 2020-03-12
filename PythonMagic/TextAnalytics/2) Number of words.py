def word_count(text): 
    count = len(text.split())   
    return count

sentence = "This is a simple test sentence."
print(word_count(sentence))



def word_count_adj(text): 
    words = text.split()
    word_count = 0
    for word in words:
        if len(word) > 1:
            word_count = word_count + 1    
    return word_count


print(word_count_adj(sentence))
