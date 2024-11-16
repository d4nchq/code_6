def split_list(input_list):
    digits = []
    letters = []
    
    for item in input_list:
        if item.isdigit():
            digits.append(int(item))
        elif item.isalpha():
            letters.append(item)
    
    return digits, letters

def main():
    #отримати ввід від користувача.
    user_input = input("Введіть список цифр і літер, розділених пробілами: ").split()
    
    #розділити список на цифри та літери.
    digit_list, letter_list = split_list(user_input)
    
    #вивести результати
    print("Список цифр:", digit_list)
    print("Список літер", letter_list)

#викликати функцію.
main()