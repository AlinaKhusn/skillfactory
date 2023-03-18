money = int(input())
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = {per_cent['ТКБ']/100 * money,
           per_cent['СКБ']/100 * money,
           per_cent['ВТБ']/100 * money,
           per_cent['СБЕР']/100 * money}
deposit = list(map(round, deposit))
print(deposit)
deposit.sort(reverse = True)
print(deposit[0])