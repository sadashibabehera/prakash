gita = " i like python i love python"
word_count = {}
for word in a.split():
   
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)