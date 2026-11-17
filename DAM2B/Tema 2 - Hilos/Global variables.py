def f():
    global i

    print(i)
    i += 1


i = 1
f()
print(i)