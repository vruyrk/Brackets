class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def push(self, val):
        return self.stack.append(val)

    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0


class MyString():
    def __init__(self):
        self.mystring = Stack()
        self.mytemp = Stack()

    def CheckBrackets(self):
        numberofbrackets = 0
        while numberofbrackets >= 0 and self.mystring.is_empty() == False:
            mytemp = self.mystring.pop()
            if mytemp == ")":
                numberofbrackets += 1
                self.mytemp.push(mytemp)
            elif mytemp == "(":
                numberofbrackets -=1
                self.mytemp.push(mytemp)

        if numberofbrackets == 0:
            print ('Balanced')
        else:
            print ('Not Balanced')

def main():
    mystring = MyString()
    mystring.mystring.stack = list('(list)')
    mystring.CheckBrackets()

main()