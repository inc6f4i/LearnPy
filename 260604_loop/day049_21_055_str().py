#031-6
intData = 1234; strData1= str(intData)
floatData1 = 1234.5; strData2 = str(floatData1)
floatData2 = 1e-3; strData3 = str(floatData2)
print(f'정수{intData}=>문자열{strData1},{type(strData1)}')
print(f'실수{floatData1}=>문자열{strData2},{type(strData2)}')
print(f'실수{floatData2}=>문자열{strData3},{type(strData3)}')