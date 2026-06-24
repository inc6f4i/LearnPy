#🌶️🌶️ [문제 2] 반도체 에칭(Etching) 가스 잔량 제어 (상급)
#실제 산업 현장에서 쓰이는 제어 로직과 유사한 문제입니다. 가스를 주입하다가 특정 조건에서 밸브를 조절하고, 위험 수위에서 비상 정지해야 합니다.
#
#<문제>
#반도체 챔버에 초기 에칭 가스가 5,000L 충전되어 있습니다.
#공정이 시작되면 매초(second) 35L씩 가스를 소모합니다.
#공정 특성상 24초마다 가스 소모량이 기존 소모량의 1.5배로 늘어납니다. (초기 35L -> 24초 후 52.5L -> 48초 후 78.75L...)
#가스를 소모한 후 잔여 가스를 체크하는데, 만약 가스 잔량이 초기 가스량의 10% 이하(500L 이하)로 떨어지면, 그 즉시 경고가 울리며 가스 소모량이 절반(0.5배)으로 급감하는 '절약 모드'가 가동됩니다.
#중요: 절약 모드는 딱 한 번만 발동되며, 절약 모드인 상태에서도 24초 주기 소모량 증가 법칙은 그대로 누적 적용됩니다.
#가스가 0 이하가 되면 공정이 종료(break)됩니다.

eGas, uGas, time = 5000, 35, 0
saverFlag = False

while True :
    time += 1
    eGas -= uGas
    if eGas <= 500 and saverFlag == False:
        saverFlag = True
        uGas *= 0.5
        print(f"{time}sec elapsed Alram : Low Gas!")
    
    while time % 24 == 0 and saverFlag == False:
        uGas *= 1.5
        break

    if eGas <= 0 :
        print(time, eGas, uGas, saverFlag)
        break

