def Word2Vect(Word):
    l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    v = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    w = Word.lower()
    wl = list(w)
    for i in range(0, len(wl)):
        if wl[i] in l:
            ind = l.index(wl[i])
            v[ind] += 1
    return v

def solve(word):

    word = word.strip()
    dictionary = open("dictionary.txt", "r")
    Words = []

    for line in dictionary:
        line = line.strip()
        
        DictVect = Word2Vect(line)
        TermVect = Word2Vect(word)
 
        isword = True

        for i in range(0,len(DictVect)):
            if DictVect[i] <=  TermVect[i]:
                isword = True
            else:
                isword = False
                break


        
        if isword == True:
            Words.append(line)
    return Words
    
if __name__ == "__main__":


    wordlist = (solve(str(input("Input Scrambled Term: "))))

    sixword = []
    fiveword = []
    fourword = []
    threeword = []
    for word in wordlist:
        if len(word) == 6:
            sixword.append(word)
        if len(word) == 5:
            fiveword.append(word)
        if len(word) == 4:
            fourword.append(word)
        if len(word) == 3:
            threeword.append(word)

    print(sixword)
    print(fiveword)
    print(fourword)
    print(threeword)