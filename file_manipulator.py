import sys

cmd = sys.argv[1]
inputpath = sys.argv[2]
contents = ''

if cmd == 'reverse':
    outputpath = sys.argv[3]

    with open(inputpath) as f:
        contents = f.read()

    with open(outputpath, 'w') as f:
        f.write(contents[::-1])

if cmd == 'copy':
    outputpath = sys.argv[3]

    with open(inputpath) as f:
        contents = f.read()

    with open(outputpath, 'w') as f:
        f.write(contents)
        
if cmd == 'depulicate-contents':
    n = sys.argv[3]
    n = int(n)

    with open(inputpath) as f:
        contents = f.read()

    with open(inputpath, 'w') as f:
        while n > 0:
            f.write(contents)
            n -= 1

if cmd == 'replace-string':
    needle = sys.argv[3]
    new_string = sys.argv[4]
    
    if needle != 'needle' or new_string != 'newstring':
        print("Try again.")
    
    with open(inputpath) as f:
        contents = f.read()

    with open(inputpath, 'w') as f:
        f.write(contents.replace(needle, new_string))
