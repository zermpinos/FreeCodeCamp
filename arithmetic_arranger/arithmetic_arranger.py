import re  # I will use this in regular expression check


def arithmetic_arranger(problems, calculate_solution=False):  # Define the function that will solve the problem and
    # return the boolean
    hardcode_space = " " * 4  # Making a variable named space so that I don't have to hardcode the spaces
    # Initializing the table
    first_line = ""
    second_line = ""
    result_line = ""
    results = ""

    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        # I am using strip to remove unwanted spaces from the number and split so that I can extract num1,2 and operator
        number = problem.strip().split()
        if len(number) != 3:  # Error handling
            return "Error: Invalid problem format."

        num1, operator, num2 = number

        if operator not in ['+', '-']:  # Error handling
            return "Error: Operator must be '+' or '-'."

        # I am checking if num1 and num2 only contain digits or a minus sign, if they are a negative number
        if not re.match(r'^-?\d+$', num1) or not re.match(r'^-?\d+$', num2):
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:  # Error handling
            return "Error: Numbers cannot be more than four digits."

        # I find the max num length and add two so that it has space to appear nice
        length = max(len(num1), len(num2)) + 2

        # I am formatting the table by adjusting the numbers to the right and adding the space I talked about earlier
        first_line += num1.rjust(length) + hardcode_space
        second_line += operator + num2.rjust(length - 1) + hardcode_space
        result_line += "-" * length + hardcode_space

        if calculate_solution:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            results += result.rjust(length) + hardcode_space

    # Create the arranged problems table
    arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + result_line.rstrip()

    # If asked for the solution boolean variable, give it
    if calculate_solution:
        arranged_problems += '\n' + results.rstrip()

    # Return the table
    return arranged_problems
