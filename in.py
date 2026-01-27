import  time

def main(func):
    lst  = []
    def outer(*args):
        start = time.time()
        num = func(*args)
        stop = time.time()
        res = stop - start
        lst.append({num: res})
        return  lst
    return  outer

@main
def deco(a, b):
    res =  a + b
    return  res
print(deco(5 , 10))
print(deco(50 , 100))

print(deco(1,3))