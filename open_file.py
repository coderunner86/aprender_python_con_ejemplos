#method 1
#file = open("spider.txt")
#print(file.readline())
#method 2
#with open("spider.txt") as file:
 #   print(file.readline())
with open("spider.txt") as file:
         for line in file:
             print(line.strip().upper())