from khaiii import KhaiiiApi


api = KhaiiiApi()


def main():
    for token in api.analyze("안녕하세요"):
        print(token)


if __name__ == '__main__':
    main()
