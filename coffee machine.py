# 결제 푸쉬 문자
def cal_money(money,price):
    a=money-price
    if money>=price:
        print("결제가 완료 되었습니다. \n현재 남은 금액:%d" %a)
    else:
        print("잔액이 부족합니다.")
        


   

# 돈을 넣는다.
#돈이 맞으면 커피 1개 줄고 커피 1개 줌
#돈이 많으면 거스름돈과 커피 줌
#600원 이상 넣었을 시에는 수량으 물어봄
#돈이 뷰족하면 돈만 줌
#커피 0 이면 기계 꺼짐


coffee =10
while True:
    money = int(input("\n잔여 커피: %d개 \n커피는 300원 입니다. \n돈을 넣어주세요: " %coffee))
    if money == 300:
        print("커피가 나옵니다")
        coffee= coffee-1
    elif 600> money > 300:
        print("커피가 나옵니다. \n거스름돈은 %d원 입니다" %(money-300))
        coffee = coffee-1
    elif money >= 600:
        number=int(input("수량을 입력해 주세요:"))
        if money == (number*300) :
            print("커피가 나옵니다")
            coffee = coffee-number
        elif money > (number*300) :
            print("커피가 나옵니다. \n거스름돈은 %d원입니다." %(money-number*300))
            coffee = coffee-number
        elif money < (number*300) :
            print("돈이 부족합니다. \n돈을 반환합니다. %d원" %money)
            coffee = coffee-number
        
    elif money<300:
        print("돈이 부족합니다. \n돈을 반환합니다. %d" %money)

    if coffee<0:
        print("기계를 중단합니다.")
        break
