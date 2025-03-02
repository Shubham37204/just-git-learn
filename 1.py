class MyClass:
    memebrship = False
    def __init__(self,name, age):
        self.name= name
        self.age = age

    def MyFun(self):
        print(f'{MyClass.memebrship}') #true
        print(f'{self.memebrship}')    #true
        print(f'{self.name}')          #shubham
        print('done')

MyName = MyClass('shubham',25)
print(MyName.name) 
print(MyName.MyFun())  #since the function does not return anything hence after printing every print statement it give a none as a output 
