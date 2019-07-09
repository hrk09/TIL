import os

os.chdir(r'C:\Users\student\TIL\startCamp\02_Day') #500개의 지원서가 있는 곳으로 이동

filenames = os.listdir('.') # .은 현재 디렉토리
for filename in filenames: # 확장자가 .txt인 파일만 이름을 바꾼다.
    extension = os.path.splitext(filename)[-1] # 확장자만 따로 분리
    if extension == '.txt':
        # print('이름을 바꾼다.', filename)
        os.rename(filename, filename.replace('SAMSUNG_SAMSUNG_','SSAFY_')) # 첫 번째 인자로 넘어간 이름을, 두 번째 인자로 넘어간 이름으로 바꾼다.
