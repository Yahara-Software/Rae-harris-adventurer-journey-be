import re
import math

def parse_instructions(instructions:str=None):
    """Retrieves the directions to travel from an md file

    Args:
        instructions (str, optional): Path to the md file. Set to Adventurer Path.md 
        if none is passed in. Defaults to None.

    Returns:
        str: string representation of directions. e.g. 5L12F
    """
    if instructions is None:instructions='Adventurer Path.md'
    with open(instructions,'r') as f:
        md_str=f.read()
        all=md_str.split("## Directions to Use\n\n")
        directions=all[len(all)-1]
        directions=directions.strip('`')
    return directions

def calc_euclidean_dist(directions:str):
    """Given a series of steps and directions to travel, this function 
    will calculate the Euclidean (straight line) distance from the starting
    point (facing North) to the final destination after following the directions

    Args:
        directions (str): A string representing the number of steps and the direction an 
        adventurer has taken. 
        For example, 6F is 6 steps forwards while 6B is 6 steps backwards
        Possible directions are:
            F = Forward/North 
            B = Back/Sourth
            L = Left/East 
            R = Right/West  

    Returns:
        float: Calculated Euclidean distance
    """
    NorthSouth=0
    EastWest=0
    
    dirArr=list(filter(None,re.split(r'([a-z,A-Z])',directions)))
    pos=0
    #Calculate the total X-axis and Y-axis distance taken from point of origin
    while pos<len(dirArr):
        steps=(int)(dirArr[pos])
        dir=dirArr[pos+1]
        if dir=='F': NorthSouth+=steps
        elif dir=='B': NorthSouth-=steps
        elif dir=='R':EastWest+=steps
        elif dir=='L':EastWest-=steps
        pos+=2
    #calculate Euclidean distance
    dist=math.sqrt(math.pow(NorthSouth,2)+math.pow(EastWest,2)) 
    return dist

def main():
    directions=parse_instructions()
    dist=calc_euclidean_dist(directions)
    return dist   

if __name__=='__main__':
    print(main())
