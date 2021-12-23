# 읽기
import csv, codecs

filename = "test.csv"
#  같은 파일 아니면, 경로 지정해주기
fp = codecs.open(filename, "r", "euc_kr")

reader = csv.reader(fp, delimiter =",", quotechar = '"')
for cells in reader:
    # print(cells)  # -> 리스트로 출력
    print(cells[0], cells[1], cells[2])
