import csv


def check_park():
    f = open('./info.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    output = ""
    for line in rdr:

        if line[1].find('공원') > 0:
            # '공원' 이라는 단어가 없으면 -1 이 출력됨
            save = line[0]+','+line[2]+','+line[3]+',1\n'
            output += save
        elif line[1].find('숲') > 0:
            # oo숲 예외 삭제파일 => Check_Park_Finish.csv 에 저장
            save = line[0]+','+line[2]+','+line[3]+',1\n'
            output += save
        else:

            save = line[0]+','+line[2]+','+line[3]+',0\n'
            output += save
    print(output)
    with open('./check_park.csv', "w", encoding="utf-8") as f:
        f.write(output)


check_park()
