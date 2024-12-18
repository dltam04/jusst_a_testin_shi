x = "tao"

def myfunc():
    global x
    x = "may"
    print("Day la " + x + ".")  

myfunc()

print("Day la " + x + ".")