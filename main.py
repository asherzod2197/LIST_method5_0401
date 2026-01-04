# CLEAR
class MyList:
    def __init__(self):
        self.data = []

    def clear(self):
        self.data = []

    def show(self):
        print(self.data)


lst = MyList()

lst.data = [10, 20, 30, 40]
lst.show()     

lst.clear()
lst.show()   
