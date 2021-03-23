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
#20210323
#지금은 한 음료만 여러개 뽑는것만 가능함
#한번에 여러개 음료를 뽑을 수는 없나...?
#먹을 콜라의 개수?:
#먹을 사이다의 개수?:
#먹을 커피 개수?:
#이런거 하면 비효율적인가..?
#해보자

coke_num = int(input("콜라 개수="))
cider_num = int(input("사이다 개수="))
coffee_num = int(input("커피 개수="))

while True:
    money = int(input("\n잔여콜라:%d\n잔여 사이다:%d\n잔여 커피:%d\n[coke]콜라(1200원)\n[cider]사이다(1000원)\n[coffee]커피(1500원)\n돈을 넣어주세요: " %(coke_num ,cider_num ,coffee_num) ))
    
    coke = int(input(" 콜라 개수="))
    cider = int(input("사이다 개수="))
    coffee = int(input("커피 개수="))

    price = coke*1200+cider*1000+coffee*1500

    if money<price:
        print("돈이 부족합니다.")
    elif money == price:
        print("음료가 나옵니다")
        coke_num= coke_num -coke
        cider_num= cider_num-cider
        coffee_num= coffee_num-coffee
    elif money>price:
        print("음료가 나옵니다. 잔돈은 %d원 입니다." %(money-price))
        coke_num= coke_num -coke
        cider_num= cider_num-cider
        coffee_num= coffee_num-coffee
    if coffee_num<=0 and coke_num<=0 and cider_num<=0:
        print("기계를 중단합니다.")
        break
