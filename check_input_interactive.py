from src.check_input import check_input

def main():
    while True:
        #print(check_input('1', [1,1,2], True))
        options = input('Give options divided by comma:')
        options = options.split(',')
        answer = input('Give answer:')
        print(check_input(answer, options, False, True))

if __name__ == '__main__':
    main()
