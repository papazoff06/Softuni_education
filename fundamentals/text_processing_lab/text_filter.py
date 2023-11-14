# banned_words = input().split(', ')
# text = input()
# for i in range(len(banned_words)):
#     word = banned_words[i]
#     if word in text:
#         text = text.replace(word, (len(word) * '*'))
# print(text)

# or
banned_words = input().split(', ')
text = input()
for word in banned_words:
    while word in text:
        text = text.replace(word, (len(word) * '*'))
print(text)