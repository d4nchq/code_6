def replace_negatives(input_list):
    #замінити від'ємні значення на 0.
    for i in range(len(input_list)):
        if input_list[i] < 0:
            input_list[i] = 0
    
    return input_list

def main():
    #отримати вхідні дані від користувача.
    user_list = list(map(int, input("Введіть список чисел: ").split()))
    
    print("Оригінальний список:", user_list)
    
    #замінити від'ємні значення на 0.
    modified_list = replace_negatives(user_list)
    
    print("Модифікований список:", modified_list)

#викликати основну функцію для виконання програми.
main()