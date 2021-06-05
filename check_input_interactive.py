from src.check_input import check_input

def main():
    while True:
        answer = input()
        print(check_input(answer, ['yes','yuno'], False))

if __name__ == '__main__':
    main()
