print("Добро Пожаловать в банкомат Беларусьбанк")
restart = ("Y")
chances = 3
balance = 1000
while chances >=0:
    pin = int(input("Пожалуйста, введите свой пин-код:"))
    if pin == (1234):
        print("Вы успешно ввели Pin-код!\n")
        while restart not in ("н","Н","Нет","НЕТ"):
            print("Нажмите 1: чтобы узнать свой баланс\n")
            print("Нажмите 2: чтобы снять деньги\n")
            print("Нажмите 3: чтобы оплатить телефон\n")
            print("Нажмите 4: вернуть карту\n")
            option = int(input("Выберите операцию:"))
            if option == 1:
                print("Ваш баланс: $",balance,"\n")
                restart = input("Хотите ли вы выйти? ")
                if restart in ("н","Н","Нет","НЕТ"):
                    print("Спасибо!")
                    break
            elif option == 2:
                option2 = ("Y")
                withdraw = float(input("Сколько вы хотите снять? 5$/10$/20$/50$/100$ :"))
                if withdraw in [5,10,20,50,100]:
                    balance = balance - withdraw
                    print("\n Ваш баланс: ", balance,"$")
                    if restart in ("н", "Н", "Нет", "НЕТ"):
                        print("Спасибо!")
                        break
                    elif withdraw != [5,10,20,50,100]:
                        print("Ошибка! Повторите попытку!")
                        restart = ("y")
                    elif withdraw == 1:
                        withdraw = float(input("Введите желаюмую сумму:"))

                elif option == 3:
                    Pay_in = float(input("Введите номер телефона:"))
                    sum = int(input("Введите сумму которую хотите зачислить на номер выше:"))
                    balance = balance-Pay_in
                    print("Ваш баланс: ", balance,"$")
                    restart = input("Хотите ли вы выйти? ")
                    if restart in ("н", "Н", "Нет", "НЕТ"):
                        print("Спасибо!")
                        break
                elif option == 4:
                    print("Ожидайте ваша карта в пути...\n")
                    print("Спасибо что выбрали нас:)")
                    break
                else:
                    print("Пожалуйста введите правильный Pin-код. \n")
                    restart = ("y")
            elif pin != ('1234'):
                    print("Неправильный Pin-код!")
                    chances = chances - 1
                    if chances == 0:
                        print("\n Не осталось попыток!")
                        break






