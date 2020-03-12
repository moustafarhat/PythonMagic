replace = {"USA": "United States of America", "UN": "United Nations"}
def replace_words(text, list):
    for i, j in list.items():
        text = text.replace(i, j)
    return text

text = "USA are a member state of the UN."

print(text)
print(replace_words(text, replace))
