import time
def paswordcheck(user_try):
    user_input = input('Please Enter a Strong password \n PASSWORD:')
    plen = len(user_input)
    if plen >= 6 and plen <= 18:
        for i in user_input:
            cnum = 0
            if i.isnumeric():
                cnum = 1
                break
        for j in user_input:
            cupp = 0
            if j.isupper():
                cupp = 1
                break
        for k in user_input:
            clow = 0
            if k.islower():
                clow = 1
                break
        for l in user_input:
            spl = ord(l)
            fsspl = 0
            if spl >= 32 and spl <= 47 or spl >= 58 and spl <= 64 or spl >= 91 and spl <= 96 or spl >= 123 and spl <= 126:
                fsspl = 1
                break
        if cnum == 1 and cupp == 1 and clow == 1 and fsspl == 1:
            print('You Entered a Strong password')
        else:
            print('Your entered password doesn\'t match the criteria')
            if user_try < 3:
                paswordcheck(user_try+1)
            else:
                print('you exceed the limit- Please try after 1 minute')
                time.sleep(6)
                paswordcheck(0)

    else:
        print('your enter password don\'t match the criteria')
        if user_try < 3:
            paswordcheck(user_try+1)
        else:
            print('you exceed the limit- Please try after 1 minute')
            time.sleep(6)
            paswordcheck(0)

paswordcheck(0)
