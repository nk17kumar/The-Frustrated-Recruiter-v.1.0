from textblob import TextBlob


s = raw_input("Why did you left your previous job?\n:")
blob = TextBlob(s)
print "\n" + str(blob.sentiment) + "\n"

s = raw_input("Why do you want to join us?\n:")
blob = TextBlob(s)
print "\n" + str(blob.sentiment) + "\n"

s = raw_input("Why should we hire you?\n:")
blob = TextBlob(s)
print "\n" + str(blob.sentiment) + "\n"
