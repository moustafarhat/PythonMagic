from nltk.stem import PorterStemmer
st = PorterStemmer()
text = "flying high landing low"
stem = [st.stem(word) for word in text.split()]
print(text)
print(stem)
