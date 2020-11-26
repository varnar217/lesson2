doing={"Как дела ?": "Хорошо!", "Что делаешь?": "Программирую"}
def ask_user():
    while True:

        bufer_string=input('пользователь\n')
    #print(doing[bufer_string])
        try :
            doing[bufer_string]
            print(doing[bufer_string])
            break

            #pass
        except KeyError:
            print ('нет вопрсса')






    #pass
ask_user()
