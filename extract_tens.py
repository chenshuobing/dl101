#coding=utf-8
f = open("幸福之路.txt")
count = {}

for line in f:
    words = line.split()
    for i in range(0,len(words)-2):
        # print "%s" % words[i]
        # print "%d" % len(words[i])
        if (len(words[i]) == 6 and len(words[i+1]) == 6):
            # print "b"
            # for word in words:
            word = words[i]  + words[i+1]
            if word in count:
               count[word] +=1
            else:
               count[word] = 1

word_freq = []
for word,freq in count.items():
    word_freq.append((freq,word));
word_freq.sort(reverse = True);

for word,freq in word_freq[:10]:
    print word,freq

# for word, counts in count.items():
    # print word , counts
