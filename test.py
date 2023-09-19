def bigger(x):
    return x ** x
x = bigger(2)
print(x)

def repeat_word (word:str, num: int) -> str:
    
    """repeat_word ("hello", 3)
    hello, hello, hello
    """
    
    result =  word + (", " + word) * (num-1)
    return result
    