def swap(x,y):
    x = x+y
    y = x-y
    x = x-y
    return print("Now x-->",x,"\n","Now y-->",y)
if __name__ == "__main__":
    x = 5
    y = 10
    swap(x, y)