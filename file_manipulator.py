import sys

cmd = sys.argv[1]
contents = ''

def reverse(inputpath, outputpath):
    outputpath = sys.argv[3]

    with open(inputpath) as f:
        contents = f.read()

    with open(outputpath, 'w') as f:
        f.write(contents[::-1])  


def copy(inputpath, outputpath):

    with open(inputpath) as f:
        contents = f.read()

    with open(outputpath, 'w') as f:
        f.write(contents)


def duplicateContents(inputpath, n):
    n = int(n)

    with open(inputpath) as f:
        contents = f.read()

    with open(inputpath, 'w') as f:
        while n > 0:
            f.write(contents)
            n -= 1  


def replaceString(inputpath, needle, newstring):
    
    if needle != 'needle' or newstring != 'newstring':
        print("Try again.")

    with open(inputpath) as f:
        contents = f.read()

    with open(inputpath, 'w') as f:
        f.write(contents.replace(needle, newstring))


if cmd == 'reverse':
    reverse(sys.argv[2], sys.argv[3])

if cmd == 'copy':
    copy(sys.argv[2], sys.argv[3])
        
if cmd == 'duplicate-contents':
    duplicateContents(sys.argv[2], sys.argv[3])

if cmd == 'replace-string':
    replaceString(sys.argv[2], sys.argv[3], sys.argv[4])
