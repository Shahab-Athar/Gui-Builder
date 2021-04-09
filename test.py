from main import Build

def hello():
    print("hello")

root = Build('Test', '300x300')

root.create()


root.label(130, 160, text = "Hello World")

btn = root.btn(130, 50, text = 'Click Me', command=lambda: hello())


root.show()
