import sys 
#명령 줄 인수 처리하기 위한 임포트


option = sys.argv[1] #옵션 -a와 v를 담기위한 변수


#-a를 치면 입력값 life is~ 를 메모장(memo.txt)에 적어줌 
if option == '-a':
    memo = sys.argv[2]            #입력 값 "Life is ~ "
    with open('memo.txt','a')as file:
        file.write(memo + '\n')  #한줄 추가 
       
#또 다른 경우로 -v를 치면 life is~ 쓰인 것을 읽어줌
elif option == '-v':
    with open('memo.txt','r')as file:   
    #with 문을 사용해 자동으로 파일을 닫게 함
        memo = file.read()
    print(memo)
        





