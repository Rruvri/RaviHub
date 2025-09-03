import datetime

current_datetime = datetime.datetime.now()
# current_datetime.strftime(%c) - formats dt correctlee

def timer():
    print(f'| {current_datetime.strftime('%c')} |')
    time.sleep(60)
    return timer()


main_body = f'| {current_datetime.strftime('%c')} |'

'''
upper_body = 
    for bound in range (0, len(main_body)-1):
        bound = '_'

        ''.join()

'''
