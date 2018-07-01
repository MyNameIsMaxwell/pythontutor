string = input()
length = len(string)
middle = int(length/2) + (length%2)
firstPart = string[:middle]
lastPart = string[middle:]

reversedString = lastPart + firstPart
print(reversedString)