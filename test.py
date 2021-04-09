from main import Build

root = Build('Test', '300x300')

root.create()


root.label(130, 160, text = "Hello World")

root.btn(130, 50, text = 'Click Me')


root.show()
