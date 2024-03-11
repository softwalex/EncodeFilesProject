import operator

#Input file to encode/decode

def encode(file):
    #Constant Value For XOR Operation
    XOR_VALUE = 5

    #Read The File
    content = bytearray(file.read())

    #Iterate Over Each Byte And XOR It With The Constant Value
    for i in range(len(content)):
        currentBit = int(content[i])
        content[i] = currentBit ^ XOR_VALUE

    #Return To The Start Of The File And Rewrite New Data
    file.seek(0)
    file.write(content)

    #Print Success Message And Close File
    print("Finished")
    file.close()

def main():
    path = input("Enter Picture Path: ")

    try:
        #Open File And Call Encode Function
        file = open(path, "rb+")
        encode(file)

    except IOError:
        print("Could not open file!")

if __name__ == "__main__":
    main()