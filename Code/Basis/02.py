def main(text: str='') -> None:
    end = sub()
    print(text + ' ' + end)

def sub() -> str:
    return 'World.'
    
main(text='Hello,')
