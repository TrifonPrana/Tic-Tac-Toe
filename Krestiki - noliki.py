import os
import colorama
os.system("cls")
#Pip install colorama

#Обьявляем цвета которые будут

colorama.init()
green = colorama.Fore.GREEN
blue = colorama.Fore.BLUE
red = colorama.Fore.RED
light_blue = colorama.Fore.LIGHTBLUE_EX

reset = colorama.Fore.RESET
 
numbers = ["1", "2", "3", "4","5", "6", "7", "8", "9"]




#Поле для игры
board = list(range(1,10))

print(board,green + "Для особо-одаренных пишем - это для системы, не для вас"+ reset)

change_symbol = input("Хотите ли вы изменить крестик и нолик на другой символ?\n" + reset)
if change_symbol == "Да" or change_symbol == "да":
    player_tokens_list = []
    print("Шаблон для символов: X, ✕, 0, O, ◯")
    tokens_symbols = input("Введите символ для крестика:\n")
    player_tokens_list.append(tokens_symbols)
    tokens_symbols = input("Введите символ для нолика:\n")
    player_tokens_list.append(tokens_symbols)
else:
    player_tokens_list = [red + "X" + reset, blue + "O" + reset]


#Счетчик ходов
counter = 0

#Флажок выигрыша
is_win = False

#Условия победы
win_coord = (
    (0, 1, 2),(3, 4, 5),(6, 7, 8),
    (0, 3, 6),(1, 4, 7),(2, 5, 8),
    (0, 4, 8),(2, 4, 6)
)


#Напишем функцию для вывода игрового поля

#Создание функции
def draw_board():
    
    #Очищаем терминал
    os.system("cls")
    
    print(green + "Игра Крестики-Нолики" + reset)
    for i in range(3):
        print(blue + "-" * 13)
        print(f"{blue}|{reset} {board[0 + i*3]} {blue}|{reset} {board[1 + i*3]} {blue}|{reset} {board[2 + i*3]} {blue}|{reset}")
    print(blue + "-" * 13)

#Начинаем игровой цикл
while not is_win:


    #Вызов функции
    draw_board()

    #А чей ход?
    if counter % 2 == 0:
        player_token = player_tokens_list[0]
    else:
        player_token = player_tokens_list[1]


    player_answer =input(light_blue + f"Ход {player_token}:\n")

    
    
    
    
    player_answer = int(player_answer) - 1
    #Проверим что ход в диапазоне допустимых значений
    if player_answer < 0 or player_answer > 8:
        print(red + "Недопустимый ход!") 
        input(green +"Чтобы продолжить нажмите Enter\n")
        
        #переходим к началу цикла
        continue




    #Ячейка свободна?
    if board[player_answer] in player_tokens_list:
        print( red + "Эта ячейка занята!")
        input(green + "Чтобы продолжить нажмите Enter\n")
        
        #переходим к началу цикла
        continue



    #Делаем ход
    board[player_answer] = player_token
    counter += 1
      




    if counter > 4:
        for each in win_coord:
                if board[each [0]] == board [each [1]] == board[each [2]]:
                    is_win = True
                    break
    if is_win:
            draw_board()
            print(f'{player_token} победил!\n'+ green)
            break
    if counter == 9:
            draw_board()
            print(green + "Победила дружба! :) \n")
            break