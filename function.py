def countingWords():
    filename=input("Enter File Name:")
    numberofwords=0
    file=open(filename)
    for count in file:
        words=count.split()
        numberofwords=numberofwords+len(words)
    print(numberofwords)
countingWords()