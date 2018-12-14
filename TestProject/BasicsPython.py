def Main():
    Exceptions()

def File():
    f = open("myfile.txt", "w")
    for i in range(4):
        f.write(input("Please enter a word: ") + '\n')
    f.close()
    fo = open("myfile.txt", "r")
    for line in fo:
        print("Updated names: " + line)
    fo.close()

    words = ["Majid", "Hamid", "Saeed", "Vahid"]

    with open("words.txt", 'w') as f1:
        for word in words:
            f1.write(word + "\n")

    f2 = open("count down.txt", "w")
    for i in range(10):
        f2.write(str(10 - i) + "\n")
    f2.close()

def Exceptions():

    try:
        f=open("students.txt", 'r')
        for line in f:
            print("Students: "+line.strip())
        f.close()
    except:
        print("File is not found or not being able to read")

    finally:
        print("Exisitng")

if __name__=="__main__":
    Main()