import parseFile
import functions
import consoleColors as cc


if __name__ == '__main__':
    functions.start(parseFile.parseFile())
    print(cc.RESET)
