def check_even_odd(input_number):
    if input_number % 2 == 0:
        return f"even"
    else:
        return f"odd" 

def calc_sum(input_number_1 , input_number_2):
    return input_number_1 + input_number_2

def analyze_sum(input_number_1 , input_number_2):
    total = calc_sum(input_number_1 , input_number_2)
    if total % 2 == 0:
        return f"The sum of {input_number_1} and {input_number_2} is {total}, and the sum is even."
    else:
        return f"The sum of {input_number_1} and {input_number_2} is {total}, and the sum is odd."
    
