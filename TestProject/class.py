class MyClass:
    number=0
    name="nonname"

def Main():
        me=MyClass()
        me.number=1337
        me.name="Majid"

        friend=MyClass()
        friend.number=3
        friend.name="Steve"

        empty=MyClass()

        print("Name: "+ me.name+ ", Favorite Number: "+str(me.number))
        print("Name: " + friend.name + ", Favorite Number: " + str(friend.number))
        print("Name: " + empty.name + ", Favorite Number: " + str(empty.number))

if __name__=='__main__':
    Main()

