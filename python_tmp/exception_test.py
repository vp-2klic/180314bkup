import sys

def test1():
    while True:
        try:
            x = int(raw_input("Pls enter a number: "))
            y = '2' + 3
            break
        except ValueError:
            print "Invalid number. Try again..."
        except TypeError:
            print "Type error. Exit..."
            break 

def test2():
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
        print i
    except IOError as e:
        print "I/O Error ({0}): {1}".format(e.errno, e.strerror)
    except ValueError:
        print "Could not convert data to integer"
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
