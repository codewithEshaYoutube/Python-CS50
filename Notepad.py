"""
emoji converter
"""

message=input("> ")
words=message.split(" ")
emoji_mapping={
        ":)" :"😊",
        ":(" :"😢",
        ";)" : "😉"
}
output=" "
output=" ".join(emoji_mapping.get(word,word)for word in words)
print (output)