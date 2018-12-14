class Reverse_Iter:

    def __init__(self, data):
        self.data=data
        self.index=len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index=self.index - 1
        return self.data[self.index]

def reverse_gener(data):
    for index in range(len(data)-1,-1 , -1): # range(start pos, end pos, step)
        yield data[index]


def Main():
    #rev=Reverse_Iter('Majid')
    rev=reverse_gener('Majid')
    for char in rev:
        print(char)

    data = 'Majid'
    print(list(data[i]  for i in range(len(data)-1,-1,-1))) # list printing

if __name__=='__main__':
    Main()
