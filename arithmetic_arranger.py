# listOfProblems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
def arithmetic_arranger(problems, withSolution=False):
    if problems.__len__() > 5:
        return "Error: Too many problems."
    elif allAreSumOrRest(problems):
        return "Error: Operator must be '+' or '-'."

    arranged_problems = ""
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    for operaciones in problems:
        digits = operaciones.split(" ")

        number1 = digits[0].strip()
        operator = digits[1].strip()
        number2 = digits[2].strip()

        if contiene_caracter_no_numerico(number1) or contiene_caracter_no_numerico(number2):
            return "Error: Numbers must only contain digits."

        if len(number1) >= 5 or len(number2) >= 5:
            return "Error: Numbers cannot be more than four digits."

        diference = getLongestNumber(number1, number2)

        first_line += "{}".format(first_line_spaces(number1, number2)) + \
            number1 + "{}".format(isLast(problems, operaciones))

        second_line += operator + "{}".format(second_line_spaces(number1, number2)) + number2 + \
            "{}".format(isLast(problems, operaciones))

        third_line += third__line_lenght(diference) + \
            "{}".format(isLast(problems, operaciones))

        operationAnswer = operation(int(number1), int(number2), operator)
        
        fourth_line += fourth_line_spaces(operationAnswer, diference) + \
            "{}".format(isLast(problems, operaciones))
        if withSolution:
            arranged_problems = first_line + "\n" + second_line + \
                "\n" + third_line + "\n" + fourth_line
        else:
            arranged_problems = first_line + "\n" + second_line + \
                "\n" + third_line
        print(arranged_problems)
    return arranged_problems


def contiene_caracter_no_numerico(cadena):
    for caracter in cadena:
        if not caracter.isdigit():
            return True
    return False


def fourth_line_spaces(operation, diference):
    leng = (diference + 2) - len(operation)
    return " " * leng + operation


def operation(number1, number2, operator):
    if operator == "+":
        return str(number1 + number2)
    elif operator == "-":
        return str(number1 - number2)


def third__line_lenght(diference):
    return "-" * (diference + 2)


def first_line_spaces(number1, number2):
    if len(number1) - len(number2) >= 0:
        return "  "
    else:
        return " " * (abs(len(number1) - len(number2)) + 2)


def second_line_spaces(number1, number2):
    if len(number2) - len(number1) >= 0:
        return " "
    else:
        return " " * (abs(len(number2) - len(number1)) + 1)


def isLast(problems, operaciones):
    if operaciones == problems[-1]:
        return ""
    else:
        return "    "


def getLongestNumber(number1, number2):
    if len(number1) > len(number2):
        return len(number1)
    else:
        return len(number2)


def allAreSumOrRest(problems):
    bool_sum = False
    for operacion in problems:
        if "*" in operacion or "/" in operacion or "//" in operacion:
            bool_sum = True
            break
    return bool_sum

arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True)