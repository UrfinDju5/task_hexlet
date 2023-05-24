number_1 = "99999999"
number_2 = "1"

def summ(number1:str, number2:str) -> str:
    if len(number1) > len(number2):
        i = len(number1) - 1
        number2 = "0" * (len(number1) - len(number2)) + number2
    else:
        i = len(number2) - 1
        number1 = "0" * (len(number2) - len(number1)) + number1
    memory = 0
    result = ""
    num = ""
    while i >= 0:              
        if int(number1[i]) + int(number2[i]) + memory > 9:
            num = int(number1[i]) + int(number2[i]) + memory
            result = str(num - 10) + result
            memory = 1
        else:
            num = int(number1[i]) + int(number2[i]) + memory
            result = str(num) + result
            memory = 0
        i -= 1
    if memory == 1:
        result = '1' + result
        return(result)
    else: 
        return(result)

print(summ(number_1, number_2))
print(int(number_1) + int(number_2))

