
# Each game consists of multiple moves
# (red, green, blue)


# ONLY  12 red cubes, 13 green cubes, and 14 blue cubes?
# 12 red cubes, 13 green cubes, and 14 blue cubes


# POSSIBLE
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

# IMPOSSIBLE
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red



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


def main():

    # Determine the max RGB
    MAX_RGB = (12, 13, 14)

    # read text file
    with open("problem_1.txt", "r") as f:
        input_text = f.readlines()

    # Transform games and moves:
    valid_games = []
    for i in input_text:
        game_num, moves = extract_game_information(i)


        # Check if valid game:
        is_valid = all([
            all(a <= b for a, b in zip(move, MAX_RGB))
            for move in moves
        ])
        
        print(f"{game_num}: {moves}: {is_valid}")

        if is_valid:
            valid_games.append(game_num)
       
    print(sum(valid_games)) 
    
    







if __name__ == "__main__":

    import os
    prev_cwd = os.getcwd()

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    main()

    os.chdir(prev_cwd)