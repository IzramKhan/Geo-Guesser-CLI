from geo_guesser import guesser
from utils.helpers import play_again
from viz.display import outro

def main():
    round_num = 1
    guesser(round_num)
    
    while True:
        again = play_again()
        
        if again:
            guesser(round_num)
            round_num += 1
        else:
            return outro()


if __name__ == '__main__':
    main()