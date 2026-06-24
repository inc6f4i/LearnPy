def mulChek(su):
    # 숫자의 가장 마지막 글자(일의 자리)를 가져옵니다.
    last_digit = str(su)[-1]
    
    # 0, 1, 3, 6, 7, 8로 끝나면 받침이 있으므로 "은", 아니면 "는"
    josa = "은" if last_digit in ["0", "1", "3", "6", "7", "8"] else "는"
    
    if su % 3 == 0:
        print(f"{su}{josa} 3의 배수입니다.")
    else :
        print(f"{su}{josa} 3의 배수가 아닙니다.")

try :
    mulChek(int(input("수 입력:")))
except :
    print("정수입력")


#pip install jamo 필요
#from jamo import hangeul_to_jamo
#
#def get_josa(text, josa_type="은는"):
#    # 입력된 텍스트(예: "3")를 한글 발음으로 변환하거나 판별하는 로직이 필요하지만,
#    # 숫자 문자열의 마지막 글자 코드값을 분석하는 것이 일반적입니다.
#    pass