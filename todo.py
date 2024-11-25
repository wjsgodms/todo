def add_task(task_name): #할 일 추가
    pass
def view_task():
    pass
def complete_task(task_number): #할 일 삭제
    pass
def delete_task(task_number):
    pass


def show_menu(): #기능 메뉴를 보여주는 함수
    print("작업 관리 애플리케이션")
    print("1. 할 일 추가")
    print("2. 할 일 목록보기")
    print("3. 할 일 완료")
    print("4. 할 일 삭제")
    print("5. 종료")

def  main():
    while True: # 무한 실행
        show_menu()
        choice = input("원하시는 기능을 선택해주세요 (1~5): ")

        if choice == '1':
            task_name = input("추가할 작업을 입력해주세요") #파이썬 공부하기
            add_task(task_name)
        elif choice == '2': #할 일 목록 보기
            view_task()
        elif choice == '3': #할 일 완료
            task_number = int(input("완료를 원하는 작업의 번호를 입력해주세요:"))
            complete_task(task_number)

        elif choice == '4':
            task_number = int(input("삭제를 원하는 작업의 번호를 입력해주세요:"))
            delete_task(task_number)
        elif choice == '5':
            print('시스템을 종료합니다.')
            break
        else:
            print("잘못 입력하셨습니다. 1번부터 5번까지의 기능 중 하나를 선택하세요.")

main()