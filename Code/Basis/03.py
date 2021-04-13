class MyClass:
    def main(self, text: str='') -> None:
        end = self.sub(subText='World.')
        self.setDelimiter()
        print(text + self.delimiter + end)
    
    def sub(self, subText: str='') -> str:
        return subText
    
    def setDelimiter(self) -> None:
        self.delimiter = ', '

myClass = MyClass()
myClass.main(text='Hello')
