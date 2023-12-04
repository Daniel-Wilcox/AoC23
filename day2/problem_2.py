
# Each game consists of multiple moves
# (red, green, blue)


# What is the minimum per game? thus what is the max colour count per move 




def convert_moves(x:str):

    def get_colour_count(x:list, colour:str = "red") -> int:
        return sum([int(i[:-len(colour)]) if colour in i else 0 for i in x])

    new_x = x.split(",")
    if new_x is None:
        return (0, 0, 0)
    
    red_count = get_colour_count(new_x, "red")
    green_count = get_colour_count(new_x, "green")
    blue_count = get_colour_count(new_x, "blue")

    return (red_count, green_count, blue_count)
    
 

def extract_game_information(x:str):

    # Remove non-critical text
    replace_text = {
        " ":"",
        "\n":"",
        "Game":"",
    }

    for k, v in replace_text.items():
        x = x.replace(k, v)

    temp_game, temp_moves = x.split(":")
    game_num = int(temp_game)

    pre_moves = [convert_moves(i) for i in temp_moves.split(";")]


    return game_num, pre_moves




def get_game_min_cubes(moves):
    max_red = 0
    max_green = 0
    max_blue = 0

    for move in moves:
        if move[0] > max_red:
            max_red = move[0]
        
        if move[1] > max_green:
            max_green = move[1]
        
        if move[2] > max_blue:
            max_blue = move[2]

    return (max_red, max_green, max_blue)



def main():

    # Determine the max RGB
    MAX_RGB = (12, 13, 14)

    # read text file
    with open("problem_1.txt", "r") as f:
        input_text = f.readlines()

    # Transform games and moves:
    power_cubes = []
    for i in input_text:
        game_num, moves = extract_game_information(i)
        max_cubes = get_game_min_cubes(moves)

        power_c = 1
        for c in max_cubes:
            power_c *= c

        print(f"{game_num}: {max_cubes} == {power_c}")
        power_cubes.append(power_c)


       
    print(sum(power_cubes)) 
    
    







if __name__ == "__main__":

    import os
    prev_cwd = os.getcwd()

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    main()

    os.chdir(prev_cwd)