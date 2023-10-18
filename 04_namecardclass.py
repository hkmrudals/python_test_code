# import sys, os, json

# class Namecard:
#     def __init__(self) -> None:
#         self.card = []
#         self.path = os.path.dirname(__file__)+ '/namecard1.json'
#         while True:
#             self.exe(self.display())
        
#     def display(self):
#         menu = input('''
# -------------------------------------------------------
#   1.입력  2.수정  3.삭제  4.목록  5.검색  6.저장  7.종료
# -------------------------------------------------------
# >>> ''')
#         return menu
#     def exe(self, menu):
#         if menu == '1':
#           self.data_input()
#         elif menu == '2':
#           self.data_update()
#         elif menu == '3':
#           self.data_delete()
#         elif menu == '4':
#           self.data_list()
#         elif menu == '5':
#           self.data_search()
#         elif menu == '6':
#           self.data_save() 
#         elif menu == '7':
#           print('프로그램 종료')
#           self.data_save()
#           sys.exit()
          
# # 명함관리 프로그램
# # 기능(입력,수정,삭제,목록,검색,종료,저장)
# # 데이터구조(이름,주소,전화번호,이메일)- 리스트
# # 데이타는 이름을 키값으로 
# # 중복된 이름은 입력 안됨.
# import json

# card = [{'name':'홍길동','address':'서울','tel':'010-1111-2222','email' : 'hong@gmail.com'},
#         {'name':'김태우','address':'세종','tel':'010-2222-3333','email' : 'kim@gmail.com'}]

# with open('02_program/namecard.json', 'r') as f:
#     card = json.load(f)

# while True:
#     menu = input('''
# -------------------------------------------------------
#   1.입력  2.수정  3.삭제  4.목록  5.검색  6.저장  7.종료
# -------------------------------------------------------
#  >>> ''')
#     if menu == '1':
#         pass
#         while True:
#             name = input('이름 >>> ')
#             check = 0
#             for item in card:
#                 if item[0] == name:
#                     check = 1
#             if check == 0:
#                 break
#             print('중복된 이름이 있습니다.')
                    
#         address = input('주소 >>> ')
#         tel = input('전화번호 >>> ')
#         email = input('이메일 >>> ')
#         card.append([name,address,tel,email])
#         print(card)
 
#     elif menu == '2':
#         name = input('수정할 이름 >>> ')
#         idx = -1
#         for index, item in enumerate(card):
#             if name == item[0]:
#                 update = int(input('수정할 항목(1.주소 2.전화번호 3.이메일)>>> '))
#                 card[index][update] = input('수정내용 입력 >>> ')
#                 break
#         if idx == -1:
#             print('등록된 데이터가 없습니다.')
                        
#     elif menu == '3':
#         name = input('삭제할 이름 >>> ')
#         delok = 0
#         for index.item in enumerate(card):
#             if item[0] == name:
#                 print(item, '삭제~')
#                 del card[index]
#                 delok = 1
#                 break
#         if delok == 0:
#             print('등록되지 않은 데이터입니다.')
    
#     elif menu == '4':
#         break
 
#     elif menu == '5':
#         name = input('검색할 이름 >>> ')
#         idx = -1
#         for index, item in enumerate(card):
#             if item[0] == name:
#                 idx = index
#                 print(f''')
                
#     {index+1}page
# --------------------------------
#     주    소 : {item[1]}
#     전화번호 : {item[2]}
#     이 메 일 : {item[3]}''')
#                 break
#         if idx == -1:
#             print('등록되지 않은 데이터입니다.') 
                 
#     elif menu == '6':
#         with open('02_program/namecard.json', 'w') as f:
#             json.dump(card,f,indent=2)
        
#     elif menu == '7':
#         print('프로그램 종료!')
#         break
#     else:
#         print('메뉴선택이 잘못되었습니다.')


'''
생성자 작성 : name, address, tel, email을 입력받아서 인스턴스를 작성
card에 내용을 적는 함수 : write_card()
card에 내용을 삭제하는 함수 : remove_all()
card객체 인스턴스를 출력하면
    name : 이름, address : 주소, tel : 전화번호, email : 이메일
'''
class Card: # 명함 1장
    def __init__(self, name='', address='', tel='', email='') -> None:
        self.name=name
        self.address=address
        self.tel=tel
        self.email=email
        
    def write_card(self, name='', address='', tel='', email=''):
        if not name == '': self.name=name
        if not address == '': self.address=address
        if not tel == '': self.tel=tel
        if not email == '': self.email=email
    
    def remove_all(self):
        self.name=''
        self.address=''
        self.tel=''
        self.email=''
        
    def __str__(self) -> str:
        return f'name : {self.name}, address : {self.address}, tel : {self.tel}, email : {self.email}'

  
'''
전체 300장의 명함을 관리할 수 있는 명함집 클래서 생성
card 객체 인스턴스는 딕셔너리로 관리한다. 키는 page_number를 사용
생성자 : 명함의 제목을 입력받아서 명함집을 만든다
이때 명함의 전체 갯수값을 가지는 변수 page_number도 초기화한다.
card를 명함집에 추가하는 함수 : add_card() 추가시 page_number값 증가
card를 명함집에서 제거하는 함수 : remove_card() 삭제시 page_number값 감소
명함집에 명함이 몇개 있는지 알려주는 함수 : get_number_of_pages():
전체 명함을 출력하는 함수 : list_card()
'''

class CardBook:
    def __init__(self, title) -> None:
        self.title = title
        self.page_number = 1
        self.cards = {}
    
    def add_card(self,card,page=0):
        if self.page_number < 300:
            if page == 0:
                self.cards[self.page_number] = card
            else:
                self.cards[page] = card
            self.page_number += 1
        else:
            print('페이지가 모두 채워졌습니다.')
    
    def remove_card(self, page):
        if page in self.cards.keys():
            return self.cards.pop()
    
    def get_number_of_pages(self):
        return len(self.cards)
    
    def list_card(self):
        for page in self.cards:
            print(self.cards[page])
    

# print(__name__)
# print('if문 밖에 namecardclass.py에서 실행')

if __name__ =='__main__':
    # print('if문 안에 namecardclass.py에서 실행')
    card = Card('홍홍홍', '세종', '999-1111-3333')
    # card1 = Card(name = '옹옹옹', email = 'ong@gmail.com')
    # print(card)
    # print(card1)
    # card.write_card('웅웅웅')
    # print(card)
    # card.remove_all()
    # print(card)
    book = CardBook('거래처')
    card = Card('홍홍홍', '세종', '000-1111-2222')
    book.add_card(card)
    book.add_card(card,5)
    print(book.get_number_of_pages())
    book.list_card()
