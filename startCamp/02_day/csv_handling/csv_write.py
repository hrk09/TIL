dinner = {
    '양자강': '02-557-4211',
    '김밥카페': '02-553-3181',
    '순남시래기': '02-508-0887',
}
# print(dinner.keys()) 은 dinner 중 '양자강', '김밥카페', '순남시래기' 키값만 뽑을 경우,

# 1. String formatting 
with open('dinner.csv', 'w', encoding="utf-8") as f:
    for item in dinner.items(): # [['양자강', '02-557-4211'], ['김밥카페', '02-553-3181'], ...]
        f.write(f'{item[0]},{item[1]}\n') # 양자강, 02-557-4221

# 2. csv writer
import csv
with open('dinner.csv', 'w', encoding="utf-8", newline='') as f: # 옵션으로 지정할 때에는 =을 붙여서 쓴다. 예) encoding=
    csv_writer = csv.writer(f) # f 라는 파일에 csv 를 작성하는 객체를 생성
    for item in dinner.items():
        csv_writer.writerow(item)
