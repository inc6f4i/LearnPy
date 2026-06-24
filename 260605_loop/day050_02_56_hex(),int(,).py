#032-3
hexStr1 = '0x11'
hexStr2 = '0x2a'

int1 = int(hexStr1, base=16) #정수형변환 16진수 형변환함수
int2 = int(hexStr2, base=16)
hexAnswer = hex(int1 + int2)
print(f'{hexStr1} + {hexStr2}= {hexAnswer}')