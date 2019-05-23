from random import randint

MONEY_PLAYER1 = 100
MONEY_PLAYER2 = 100
def main():
    while MONEY_PLAYER1 >0 and MONEY_PLAYER2 > 0:
        def get_rate():
            rate1 = 1
            rate2 = 2
            while True:
                try:
                    rate1 = int(input('Пусть Игрок1 сделает ставку:'))
                    rate2 = int(input('Пусть Игрок2 сделает ставку:'))
                    if rate1 > MONEY_PLAYER1:
                        print("У Игрока1 нет столько денег. Сделайте ставки снова.")
                        continue
                    elif rate2 > MONEY_PLAYER2:
                        print("У Игрока2 нет столько денег. Сделайте ставки снова.")
                        continue
                    elif rate1 != rate2:
                        print('Ваши ставки не совпали. Придите к согласию и сделайте ставки снова.')
                        continue
                    elif rate1 == rate2:
                        return rate1
                except ValueError:
                    print("Можно вводить только целые цифры. Повторите ввод.")
                    continue

        rate = get_rate()

        def throw_dice():
            print('\nИгрок1, для того, чтобы бросить кубики, нажмите Enter')
            input()
            print("Парам-пам-пам....")
            p1_dice1 = randint(1, 6)
            p1_dice2 = randint(1, 6)
            p1_dice_sum = p1_dice1 + p1_dice2
            print("ИГРОК 1 \nПервый кубик: %s.\nВторой кубик: %s. \nСумма кубиков: %s." % (
            p1_dice1, p1_dice2, p1_dice_sum))

            print('\nИгрок2, для того, чтобы бросить кубики, нажмите Enter')
            input()
            print("Парам-пам-пам....")
            p2_dice1 = randint(1, 6)
            p2_dice2 = randint(1, 6)
            p2_dice_sum = p2_dice1 + p2_dice2
            print("ИГРОК 2 \nПервый кубик: %s.\nВторой кубик: %s. \nСумма кубиков: %s." % (
            p2_dice1, p2_dice2, p2_dice_sum))

            return p1_dice_sum, p2_dice_sum

        print('\nПервый бросок')
        Throw1 = throw_dice()
        print('\nВторой бросок')
        Throw2 = throw_dice()
        print('\nТретий бросок')
        Throw3 = throw_dice()

        print('\n\n\n')




        def check_step():
            global MONEY_PLAYER1
            global MONEY_PLAYER2
            total_p1 = Throw1[0] + Throw2[0] + Throw3[0]
            print("Игрок1 сумма очков по трем броскам:", total_p1)
            total_p2 = Throw1[1] + Throw2[1] + Throw3[1]
            print("Игрок2 сумма очков по трем броскам:", total_p2)
            if total_p1 > total_p2:
                MONEY_PLAYER1 += rate
                MONEY_PLAYER2 -= rate
                print("Игрок1 забирает ставку, у него на счету", MONEY_PLAYER1)
            elif total_p1 < total_p2:
                MONEY_PLAYER1 -= rate
                MONEY_PLAYER2 += rate
                print("Игрок2 забирает ставку, у него на счету", MONEY_PLAYER2)
            else:
                print("Очки совпали: ничья. Ставка никому не досталась.")

        check_step()
        #В функции нет смысла, но я добавил, чтобы сгруппировать код как-бы

    if MONEY_PLAYER1 > 0:
        print('Победил первый игрок, у него 200 баксов')
    if MONEY_PLAYER2 > 0:
        print('Победил второй игрок, у него 200 баксов')
    print("Поздравляем! \nИгра окончена.")

main()


