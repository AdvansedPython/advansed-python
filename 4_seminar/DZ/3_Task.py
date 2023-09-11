# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


money = 0.0
count_operations = 0
sum_operations = 0.0


def print_menu():
    global money
    print(f"\nНа вашем счету: {money}\n\
Введите действие:\n\
пополнить   (+)\n\
снять       (-)\n\
выйти       (q)\n")
    

def user_money_value():
    while True:
        insert_money = input("Введите сумму:\n")
        if insert_money == "" or not insert_money.isdigit() or+ int(insert_money) % 50 != 0:
            print("Сумма должна быть кратна 50!\n")
            continue
        break
    return insert_money

def accrual():
    global money, count_operations
    if count_operations == 3:
        procents = money * 3 / 100
        money += procents
        count_operations = 0
        print(f"Начислено {procents} процентов")

def wealth_tax():
    global money

    if money > 5_000_000.0:
        procents = money * 10 / 100
        money -= procents
        print(f"Налог на богатство {procents} процентов")

def invest():
    global money, count_operations

    count_operations += 1
    wealth_tax()
    money += int(user_money_value())

    accrual()


def remove_money():
    global money, count_operations
    
    user_money = float(user_money_value())
      
    wealth_tax()
    percents = float(user_money) * 1.5 / 100
    if percents < 30.0:
        percents = 30.0
    elif percents > 600.0:
        percents = 600.0

    if user_money + percents > money:
        print("На счете не хватает средств(")
        return  
    
    money -= user_money + percents
    count_operations += 1
    print(f"Снято {user_money} денежных единиц и {percents} в проценты банку")
    
    accrual()


def start_bank():
    while True:
        print_menu()
        
        match input().lower():
            case("+"):
                invest()
            case("-"):
                remove_money()
            case("q"):
                break


start_bank()

