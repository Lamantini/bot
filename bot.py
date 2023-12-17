phone_dict = {}


def input_error(func):
    def inner(request):
        try:
            result = func(request)
        except KeyError:
            return 'Enter user name'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Give me name and phone please'
        return result
    return inner


@input_error
def handler_add(request):
    n_p = request.split(' ')
    phone_dict.update({n_p[1]: n_p[2]})
    answer = 'Added'
    return answer


@input_error
def handler_change(request):
    n_p = request.split(' ')
    phone_dict[n_p[1]] = n_p[2]
    answer = 'Changed'
    return answer


@input_error
def handler_phone(request):
    n_p = request.split(' ')
    number = phone_dict[n_p[1]]
    return number


def main():

    while True:
        request = input('')
        if request.lower() == 'hello':
            print('How can I help you?')
        elif request.startswith('add'):
            answer = handler_add(request)
            print(answer)
        elif request.startswith('change'):
            answer = handler_change(request)
            print(answer)
        elif request.startswith('phone'):
            number = handler_phone(request)
            print(number)
        elif request.startswith('show all'):
            print(phone_dict)
        elif request.lower().startswith(('good bye', 'close', 'exit')):
            print('Good bye!')
            return False


if __name__ == '__main__':
    main()