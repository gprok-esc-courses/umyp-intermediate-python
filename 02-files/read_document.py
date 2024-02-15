
file = open('document.txt')

lines = file.readlines()

counter = 0
sentence_counter = 0
word_counter = 0
for line in lines:
    if len(line.strip()) > 0:
        counter += 1
        sentences = line.strip().split('.')
        for sentence in sentences:
            sentence_counter += 1
            words = sentence.split(' ')
            for word in words:
                word_counter += 1

print(counter)
print(sentence_counter)
print(word_counter)

