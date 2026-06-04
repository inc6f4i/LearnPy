#020-1
http_status = int(input())

match http_status:
    case 400:
        print('Bad request')
    case 401:
        print('Unaruthorized')
    case 403:
        print('Forbidden')
    case 404:
        print('Not found')
    case _:
        print('기타인터넷 문제로 뭔가 잘못됨')