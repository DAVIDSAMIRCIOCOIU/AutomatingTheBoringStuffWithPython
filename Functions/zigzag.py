import time,sys
indent = 0
indentIncreasing = True

try:
    while True:
        print(' '*indent, end='')
        print('********')
        time.sleep(0.05)  # pause for 1/10 of a second

        if indentIncreasing:
            indent += 1
            if indent == 20:
                indentIncreasing = False  # change direction

        else:
            #  Decrease n of spaces
            indent -= 1
            if indent == 0:
                # Change direction
                indentIncreasing = True
except KeyboardInterrupt:  # control + c
    sys.exit()