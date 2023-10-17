'''
반장선거에서 투표한 후보자 번호들을 공백을 구분자로 하여 입력하면
각 값들을 분리하고 분리한 값들은 숫자로 변경하여
각 숫자별로 같은 값의 갯수를 체크하여 출력하는 프로그램
함수는 아래와 같이 작성
- 공백을 구분자로 하여 입력받은 후보자 번호를 분리하는 함수
- 숫자로 변경된 값들의 항목별로 갯수를 카운트 하는 함수
- 결과값을 출력하는 함수
입력 예 = 1 2 4 5 3 4 2 1 2
출력 예 = 기호 : 1 득표수 : 2
         기호 : 2 득표수 : 3
         기호 : 3 득표수 : 4
         기호 5번까지
'''

# def str2int(s):
#     try:
#         result = int(s)
#         return result
    
#     except ValueError:
#         print("올바른 정수 문자열이 아닙니다.")    
#         return None

# def countvotes(numbers):
#     vote_count = {}
    
#     for number in numbers:
#         if number in vote_count:
#             vote_count[number] += 1
#         else:
#             vote_count[number] = 1
#     return vote_count
        
# def printresult(vote_count):
#     for number, count in vote_count.items():
#         print(f"후보자 번호 {number}: {count} 표")


 


