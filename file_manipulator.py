import sys

if sys.argv[0] != "file_manipulator.py":
    print("1番目の引数には\nfile_manipulator.py\nに設定してください。")
    sys.exit()

if sys.argv[1] != "reverse" and "copy" and "duplicate-contents" and "replace-string":
    print(
        "reverse, copy, duplicate-contents, replace-string 以外のコマンドは使用できません。"
    )
    sys.exit()

cmd = sys.argv[1]
inputpath = sys.argv[2]
sys_argv_length = len(sys.argv)
contents = ""


def reverse(inputpath, outputpath):
    outputpath = sys.argv[3]

    with open(inputpath) as f:
        contents = f.read()

    with open(outputpath, "w") as f:
        f.write(contents[::-1])

    print(outputpath + " に " + inputpath + " の内容を逆にして反映させました。")


def copy(inputpath, outputpath):

    with open(inputpath) as f:
        contents = f.read()

    with open(outputpath, "w") as f:
        f.write(contents)

    print(inputpath + " のコピーを " + outputpath + " として作成しました。")


def duplicateContents(inputpath, n):
    n = int(n)
    g = str(n)

    with open(inputpath) as f:
        contents = f.read()

    with open(inputpath, "w") as f:
        while n > 0:
            f.write(contents)
            n -= 1

    print(inputpath + " の内容を同ファイルに " + g + " 回複製しました。")


def replaceString(inputpath, needle, newstring):
    with open(inputpath) as f:
        contents = f.read()

    with open(inputpath, "w") as f:
        f.write(contents.replace(needle, newstring))

    print(inputpath + " の文字列 needle を全て newstring に置換しました。")


if cmd == "reverse":
    if sys_argv_length < 4 or sys_argv_length > 4:
        print(
            "3番目・4番目の引数には\nコピー元ファイル名, コピー先ファイル名(新規も可)\nを適切に設定してください。"
        )
        sys.exit()

    reverse(inputpath, sys.argv[3])

if cmd == "copy":
    if sys_argv_length < 4 or sys_argv_length > 4:
        print(
            "3番目・4番目の引数には\nコピー元ファイル名, コピー先ファイル名(新規も可)\nを適切に設定してください。"
        )
        sys.exit()

    copy(inputpath, sys.argv[3])

if cmd == "duplicate-contents":
    if sys_argv_length < 4 or sys_argv_length > 4:
        print(
            "3番目・4番目の引数には\n既存ファイル名, 実行回数\nを適切に設定してください。"
        )
        sys.exit()

    duplicateContents(inputpath, sys.argv[3])

if cmd == "replace-string":
    if sys.argv[3] != "needle" or sys.argv[4] != "newstring":
        print("4番目・5番目の引数には\nneedle, newstring\n に設定してください。")
        sys.exit()

    replaceString(inputpath, sys.argv[3], sys.argv[4])
