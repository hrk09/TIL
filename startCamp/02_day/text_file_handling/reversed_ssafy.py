# ssafy.txt 파일 읽어서
# 역순으로 reversed_ssafy.txt 파일로 저장
with open('ssafy.txt', 'r') as f:
    lines = f.readlines() # 각 라인을 item으로 리스트의 형태로 반환(역순작업을 리스트로 하는 것이 좋으므로 readlines)
    # print(lines)

lines.reverse() # list 를 반대로 뒤집는다.

with open('reversed_ssafy.txt', 'w') as f:
    for line in lines:
        f.write(line)
