class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if Singleton.instance is None:
            Singleton.instance = super().__new__(cls)
            Singleton.db_connection(Singleton.instance)
        return Singleton.instance

    def db_connection(self):
        print("db connection processing...")
        self.data = 101


if __name__ == '__main__':
    first_try = Singleton()
    print(first_try)
    second_try = Singleton()
    print(second_try)
    print(first_try is second_try)
    print(first_try.data)
    first_try.data = 202
    print(second_try.data)
