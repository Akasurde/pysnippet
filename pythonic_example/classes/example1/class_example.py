class Greetings(object):
    def __init__(self):
        print("Init is called")

    def say_hello(self):
        print("hello")


def main():
    greeting = Greetings()
    greeting.say_hello()

if __name__ == '__main__':
    main()
