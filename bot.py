phone_dict = {}


def main():
    while True:
        request = input('')
        if request.lower() == 'hello':
            print('How can I help you?')
        else:
            print('not hello')
main()