#백준 1302 베스트셀러

book_dict = {}
alphabet_list = []
N = int(input("팔린 책의 개수를 입력해주세요: "));
for i in range(N):
    bookname = input("팔린 책의 이름을 입력 후 Enter를 눌러주세요: ")
    #Collection의 Counter를 사용해서 자동으로 딕셔너리로 집계할 수 있음
    if bookname in book_dict.keys():
        book_dict[bookname] += 1
    else:
        book_dict[bookname] = 1

selled = list(book_dict.values())
selled.sort()
bestseller = selled[-1]
for sell in book_dict:
    if book_dict[sell] == bestseller:
        alphabet_list.append(sell)
alphabet_list.sort() # sort는 시간 복잡도가 크므로 바꿔보기
print(alphabet_list[0])
