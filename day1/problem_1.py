# Initial thoughts are that each line has a set of letters & numbers. 
# These calibration numbers for each line are the numbers within the text


# Example
# 1abc2 -> 12
# pqr3stu8vwx -> 38
# a1b2c3d4e5f -> 12345
# treb7uchet -> 7
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Rules:
# 0. Remove all letters
# 1. If only 1 number, return that * 11
# 2. If only 2 numbers, return that
# 3. If more than 2 numbers, return first-last number combo






def _keep_digits(x:str) -> int:
    # Lowercase and remove non-numerics
    new_x = [i for i in x.lower() if i.isdigit()]

    len_x = len(new_x)

    # Apply rules for numbers
    if len_x == 0:
        return 0
    
    elif len_x == 1:
        return int(new_x[0])*11
    
    else:
        return int(new_x[0] + new_x[-1])


def validation():

    example_text = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]
    example_answer = [12, 38, 15, 77]

    # read text file
    input_text = example_text

    # convert to digits
    converted_num = [_keep_digits(x) for x in input_text]
    print(f"expected: {example_answer}")
    print(f"actual: {converted_num}")
    
    # Sum values
    final_sum = sum(converted_num)
    validated_sum = sum(example_answer)

    if final_sum == validated_sum:
        print("Summed answers correct")
    else:
        print("Summed answers incorrect")

    return

    

def main():
    import os
    prev_cwd = os.getcwd()

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)


    # read text file
    with open("problem_1.txt", "r") as f:
        input_text = f.readlines()


    # convert to digits
    converted_num = [_keep_digits(x) for x in input_text]
    print(converted_num)
    
    # Sum values
    print(sum(converted_num))

    os.chdir(prev_cwd)



if __name__ == "__main__":
    # validation()
    main()