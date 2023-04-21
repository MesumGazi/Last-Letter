def log(word):
    word2=input("")
    if word2[0]!=word[len(word)-1]:
        print("YOU LOOSE!")
        print("score",score_count)
    else:
        print("ENTER A NEW WORD STARTING WITH THE LETTER ",word2[len(word2)-1])
        
    return word2