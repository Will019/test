def hello(name,age):
    if age < 18:
        print("Hello %s, you are a kid!" % (name))
    elif age < 50:
        print("Hello %s, you are an adult!" % (name))
    else:
        print("Hello %s, you are ooooold!" % (name))

name=str(input("What is your name?: "))
age=int(input("How old are you?: "))

hello(name,age)
