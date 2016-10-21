while True:
    try:
        number =  int(input('Put your number!\n'))
        res = 18 / number
        print(res)
        break
    except ValueError:
        print('Put a number, please!')
    except ZeroDivisionError:
        print('Put anything but not zero!')
    finally:
        print('New iteration!')