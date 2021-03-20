# 돈을 넣는다.
#돈이 맞으면 커피 1개 줄고 커피 1개 줌
#돈이 많으면 거스름돈과 커피 줌
#600원 이상 넣었을 시에는 수량으 물어봄
#돈이 뷰족하면 돈만 줌
#커피 0 이면 기계 꺼짐
#2021.3.14
#커피 개수보다 더 많이 주문 했을때 안된다는걸 나타내는 기능 
#맨 처음에 관리자가 커피를 넣어보는기능 추가...

#20210320
#새로운 기능
#종류 다른 음료 한번에 뽑기


coke = int(input(" 콜라 개수="))
cider = int(input("사이다 개수="))
coffee = int(input("커피 개수="))

while True:
    money = int(input("\n잔여콜라:%d\n잔여 사이다:%d\n잔여 커피:%d\n[coke]콜라(1200원)\n[cider]사이다(1000원)\n[coffee]커피(1500원)\n돈을 넣어주세요: " %(coke ,cider ,coffee) ))
    
    drink = str(input("먹을 음료를 골라주세요:"))
    
    if drink=='coke':
        if money == 1200:
            print("콜라가 나옵니다")
            coke= coke-1
        elif 2400> money > 1200:
            print("콜라가 나옵니다. \n거스름돈은 %d원 입니다" %(money-1200))
            coke = coke-1
        elif money >= 2400:
            number=int(input("수량을 입력해 주세요:"))
            if money == (number*1200) :
                print("사이다가 나옵니다")
                coke = coke-number
            elif money > (number*1200) :
                if number > coke:
                    print("수량이 부족합니다. 지금 뽑을 수 있는 최대 수량은 %d 입니다. 다시 주문해주세요" %coke)
                else:
                    print("콜라가 나옵니다. \n거스름돈은 %d원입니다." %(money-number*1200))
                coke = coke-number
            elif money < (number*1200) :
                print("돈이 부족합니다. \n돈을 반환합니다. %d원" %money)
            
    if drink=='cider':
        if money == 1000:
            print("사이다가 나옵니다")
            cider= cider-1
        elif 2000> money > 1000:
            print("사이다가 나옵니다. \n거스름돈은 %d원 입니다" %(money-1000))
            cider = cider-1
        elif money >= 2000:
            number=int(input("수량을 입력해 주세요:"))
            if money == (number*1000) :
                print("사이다가 나옵니다")
                cider = cider-number
            elif money > (number*1000) :
                if number > cider:
                    print("수량이 부족합니다. 지금 뽑을 수 있는 최대 수량은 %d 입니다. 다시 주문해주세요" %cider)
                else:
                    print("사이다가 나옵니다. \n거스름돈은 %d원입니다." %(money-number*1000))
                cider = cider-number
            elif money < (number*1000) :
                print("돈이 부족합니다. \n돈을 반환합니다. %d원" %money)
                
    if drink=='coffee':
        if money == 1500:
            print("커피가 나옵니다")
            coffee= coffee-1
        elif 3000> money > 1500:
            print("커피가 나옵니다. \n거스름돈은 %d원 입니다" %(money-1500))
            coffee= coffee-1
        elif money >= 3000:
            number=int(input("수량을 입력해 주세요:"))
            if money == (number*1500) :
                print("커피가 나옵니다")
                coffee= coffee-number
            elif money > (number*1500) :
                if number > coffee:
                    print("수량이 부족합니다. 지금 뽑을 수 있는 최대 수량은 %d 입니다. 다시 주문해주세요" %coffee)
                else:
                    print("커피가 나옵니다. \n거스름돈은 %d원입니다." %(money-number*1500))
                coffee= coffee-number
            elif money < (number*1500) :
                print("돈이 부족합니다. \n돈을 반환합니다. %d원" %money)            
    

    if coffee<=0 and coke<=0 and cider<=0:
        print("기계를 중단합니다.")
        break
