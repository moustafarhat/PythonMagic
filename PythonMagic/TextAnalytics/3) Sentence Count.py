import re

def sentence_count(text):	
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text) 
    count = len(sentences) 
    return count

sentences = "This is the first test sentence. This is the second test sentence? This is the thid test sentence"

print(sentences)
print(sentence_count(sentences))
