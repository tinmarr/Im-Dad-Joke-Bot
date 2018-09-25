import re

phrase = input("Please describe yourself in one complete sentence:")
if re.search("i am", phrase, re.IGNORECASE):
    phrase = phrase.lower()
    words = phrase.split()
    a = words.index("i")
    b = words.index("am")
    del words[a]
    del words[b - 1]
    phrase = " ".join(words)

elif re.search("i'm", phrase, re.IGNORECASE):
    phrase = phrase.lower()
    words = phrase.split()
    a = words.index("i'm")
    del words[a]
    phrase = " ".join(words)

print(f"Hi {phrase}! I'm Dad!")
