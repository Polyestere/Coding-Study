#백준 2711 오타맨 고창영

case_list = []
answer_list = []
T = int(input("테스트 케이스의 개수를 입력해주세요: "));
for i in range(T):
    cases = input("오타 위치를 숫자로 입력하고 띄어쓰기 후 문자열을 입력해 주세요:  ").split()
    case_list.append(cases)
for i in range(T):
    slice_loc = int(case_list[i][0])
    slice_str = case_list[i][1]
    part1 = slice_str[:(slice_loc-1)]
    part2 = slice_str[(slice_loc):]
    fixedstr = part1 + part2
    answer_list.append(fixedstr)

for i in range(len(answer_list)):
    print(answer_list[i])
