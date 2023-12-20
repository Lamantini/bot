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
    if n_p[1] not in phone_dict:
        phone_dict.update({n_p[1]: n_p[2]})
        answer = 'Added'
    else:
        answer = 'This name is already exist'
    return answer


@input_error
def handler_change(request):
    n_p = request.split(' ')
    if n_p[1] in phone_dict:
        phone_dict[n_p[1]] = n_p[2]
        answer = 'Changed'
    else:
        answer = 'This name is not exist'
    return answer


@input_error
def handler_phone(request):
    n_p = request.split(' ')
    number = phone_dict[n_p[1]]
    return number


OPERATIONS = {
            'add': handler_add,
            'change': handler_change,
            'phone': handler_phone
        }


def main():

    while True:
        request = input('')
        request = request.lower()
        if request == 'hello':
            print('How can I help you?')
        elif request.startswith('show all'):
            print(phone_dict)
        elif request.startswith(('good bye', 'close', 'exit')):
            print('Good bye!')
            return False
        else:
            handler = get_handler(request)
            print(handler(request))


def get_handler(request):
    if request.split(' ')[0] in OPERATIONS:
        return OPERATIONS[request.split(' ')[0]]
    else:
        return (lambda x: 'Give me correct command')


if __name__ == '__main__':
    main()