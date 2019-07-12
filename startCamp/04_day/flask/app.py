from flask import Flask, render_template, request # 사용자의 요청 확인 가능
import requests
import random
app = Flask(__name__)


@app.route('/') # / => root
def index():
    return 'Hello world'


@app.route('/greeting/<string:name>')
def greeting(name):
    return render_template('greeting.html', name=name)  


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    age = request.args.get('age')
    return f'Pong! age: {age}'


@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/naver')
def naver():
    return render_template('naver.html')


@app.route('/op_gg_ow')
def op_gg_ow():
    return render_template('op_gg_ow.html')


@app.route('/ascii_input')
def ascii_input():
    return render_template('ascii_input.html')


@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text') # input의 name을 text로 보냈으므로
    # Ascii art API 활용하여 사용자의 input 값을 변경한다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    result = response.text
    return render_template('ascii_result.html', result=result)

@app.route('/lotto_input') # 사용자가 입력할 수 있는 페이지만 전달
def lotto_input():
    return render_template('lotto_input.html')


@app.route('/lotto_result')
def lotto_result():
    # 사용자 입력값 받기
    lotto_round = request.args.get('round')
    lotto_numbers = request.args.get('numbers').split() # ['1', '2', ..]
    # print(lotto_numbers.split()) # 6 자리 숫자를 콘솔창에서 리스트 형태로 출력되게 만드는 것 split()
      
    
    #  당첨 번호 확인
        # url 가져와서 lotto_numbers와 비교
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)
    lotto_info = response.json()
    winner = [] # [1, 2, ..]
    for i in range(1, 7):
        winner.append(str(lotto_info[f'drwtNo{i}']))
    
    # print(lotto_numbers)  # 사용자 도전번호
    # print(winner)         # 실제 당첨번호
    
    # 번호 교집합 개수 찾기
    if len(lotto_numbers) == 6:         # 사용자 숫자가 딱 6개가 맞는 지 확인
        matched = 0 
        for number in lotto_numbers:    # 사용자 숫자를 하나씩 확인하면서
            if number in winner:        # 당첨번호에 있는지 체크해서
                matched += 1            # 당첨 시 matched 를 1 씩 증가
    
        if matched == 6:
            result = '1등'
        elif matched == 5:
            if str(lotto_info['bnusNo']) in lotto_numbers:
                result = '2등'
            else:
                result = '3등'
        elif matched == 4:
            result = '4등'
        elif matched == 5:
            result = '5등'
        else:
            result = '다음기회에..'
    else:
        result = '입력하신 숫자가 6개가 아닙니다.'

    return render_template('lotto_result.html', result=result)


#     return f'{lotto_round}, {lotto_numbers}' # json 타입의 파일을 python dictionary 로 parsing 해줘
    
   

if  __name__ == '__main__':
    app.run(debug=True)
