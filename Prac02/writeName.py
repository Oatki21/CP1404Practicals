name = str(input("What is your name? "))
outFile = open("name.txt", "w")# stands for write and r stands for read
print(name, file=outFile) # or outFile.write(name)
outFile.close()