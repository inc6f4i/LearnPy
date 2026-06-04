#020-2
http_status = int(input())
match http_status:
    case 200|202|203:
        print('Success')
    case 301|302|303:
        print('Redirection')
    case 400|401|403|404:
        print('Client Errors')
    case _:
        print('기타 HTTP응답코드')