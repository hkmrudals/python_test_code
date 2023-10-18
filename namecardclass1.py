import namecardclass as ncc
import sys, pickle, os

'''
1. CardBook 생성 2. Card 추가 3. Card 삭제 4. Card 보기 5. 전체목록 6. 종료
프로그램 시작되면 데이터 파일을 로드
프로그램 종료되면 데이터 파일을 저장
'''

path = os.path.dirname(__file__)+'/cardbook.pickle'
try : 
    with open(path, 'rb') as f:
        cardbook = pickle.load(f)
except FileNotFoundError:
    print('데이터 파일이 아직 생성되지 않았습니다.')
    
while True:
    menu = input('''
-------------------------------------------------------
  1.입력  2.수정  3.삭제  4.목록  5.검색  6.저장  7.종료
-------------------------------------------------------
 >>> ''')
    if menu == '1':
      pass
 
    elif menu == '2':
      pass
                        
    elif menu == '3':
      pass
    
    elif menu == '4':
      pass
 
    elif menu == '5':
      pass
                 
    elif menu == '6':
      print('프로그램 종료')
      sys.exit()
        
    else:
        print('메뉴선택이 잘못되었습니다.')
        