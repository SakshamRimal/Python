# # open("FILEname" , "mode")

f1 = open('File_1' , "w+")
# print(f1.tell())
# # first we have to create a file then only we can use mode otherwise it will give an error
# # f1 = open('File_2' , "r") since there is no file_2 so it will give us error
# # f1 = open('File_1' , "x") name same hunu hudena different hunu parxa file chai 

# # data = f1.read()
# # print(data) 
# # since in file we have written a lie so it read the line and print it 

# # print(f1.read())
# # f1.write("Something")

# # if we open the file now in write mode the perivious conetnet will be erased and it will override the content
# # print(f1.tell())
# # f1.write("Hi")
# # print(f1.tell())
# # print(f1.read())
# # print(f1.tell())

# f1.write("Hi Welcome")
# print(f1.tell())
# f1.seek(0)
# data = f1.read()
# print(f1.tell())
# print(data)
# print(f1.tell())

# # why there is noany output?
# # because when we write the cursor is moved to place wehere there is nothing so it will not show anythung
# # after using seek(0) the position is in 0th position and now we can write the file
f1.close() # close garyo bhane data ni janxa 

f1 = open('File_1' ,'a+')
f1.write("Hello Students") 
# f1.read() in append mode we can only wrtie 
# in a+ we can append and read
# f1.seek(0) #0th position ma janxa cursor ani tya bata read hunxa conetent haru 
print(f1.read())

f1.write("File handling is boring")
f1.seek(0)
print(f1.read())






