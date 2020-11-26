def hello_user():
    while True:
        try:
            a=input('Как дела?\n')
            if a =='Хорошо':
                break
            else:
                pass
        except KeyboardInterrupt:
            print('Пока!')
            break           
hello_user()
