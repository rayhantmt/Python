def word(sentence):
    print(sentence)
    def ss(word):
       print(word)
    words=sentence.split(" ")
    for word in words:
        ss(word)


word("my name is rayhan i am a flutter developer and i am learning python")
