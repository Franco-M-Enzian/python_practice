pathname = 'test.txt'

file = open(pathname)
contents = file.read()
file.close()

file = open(pathname, 'w')
file.write(contents + "HELLO")
file.close()
