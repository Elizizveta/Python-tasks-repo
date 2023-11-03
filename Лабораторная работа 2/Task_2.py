money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов


n=0
free = money_capital + salary
while free >= 0:
    free = free - spend
    if free < 0:
        break
    spend = spend * 1.05
    free = free + salary
    n=n+1
print("Количество месяцев, которое можно протянуть без долгов:", n)