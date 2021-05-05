def add(x,y):
    if(
        y == 0
    ) : return x

    else: return add((x^y), (x & y) << 1)
    
if __name__ == "__main__":
    print(add(32, 4))