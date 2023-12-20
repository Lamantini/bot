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


def main():

    while True:
        request = input('')
        if request.lower() == 'hello':
            print('How can I help you?')
        elif request.lower().startswith('add '):
            answer = handler_add(request)
            print(answer)
        elif request.lower().startswith('change '):
            answer = handler_change(request)
            print(answer)
        elif request.lower().startswith('phone '):
            number = handler_phone(request)
            print(number)
        elif request.lower().startswith('show all'):
            print(phone_dict)
        elif request.lower().startswith(('good bye', 'close', 'exit')):
            print('Good bye!')
            return False


if __name__ == '__main__':
    main()