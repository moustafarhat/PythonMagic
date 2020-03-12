import re

def word_count(text): 
    count = len(text.split())   
    return count

def sentence_count(text):	
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text) 
    count = len(sentences) 
    return count

def avg_sentence_length(text): 
    words = word_count(text)
    sentences = sentence_count(text)
    return words/sentences

sentences = "This is the first test sentence. This is the second test sentence? This is the thid test sentence"

print(sentences)
print(avg_sentence_length(sentences))
