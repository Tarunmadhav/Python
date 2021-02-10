intro=input("Introduction:")
chracterCount=0
wordCount=1
for i in intro:
    chracterCount=chracterCount+1
    if(i==" "):
        wordCount=wordCount+1

print(chracterCount)
print(wordCount)