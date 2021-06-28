#import traceback

from src.check_input import check_input

def main():
    while True:
        #print(check_input('1', [1,1,2], True))
        options = input('Give options divided by comma:')
        options = options.split(',')
        for i, option in enumerate(options):
            integer, floa = None, None
            try:
                integer = int(option)
            except Exception as e:
                #traceback.print_exc()
                pass
            try:
                floa = float(option)
            except Exception as e:
                #traceback.print_exc()
                pass
            if integer is not None:
                option = integer
            elif floa is not None:
                option = floa
            print(i, option.__class__)
            options[i] = option

        answer = input('Give answer:')
        integer, floa = None, None
        try:
            integer = int(answer)
        except Exception as e:
            #traceback.print_exc()
            pass
        try:
            floa = float(answer)
        except Exception as e:
            #traceback.print_exc()
            pass
        if integer is not None:
            answer = integer
        elif floa is not None:
            answer = floa
        print(i, answer.__class__)

        print(check_input(answer, options, False, True))

if __name__ == '__main__':
    main()
