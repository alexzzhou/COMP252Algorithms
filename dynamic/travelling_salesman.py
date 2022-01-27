import math
import typing

def calcDistance(a: typing.Tuple[int, int], b: typing.Tuple[int, int]):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def helper(cities: typing.List[typing.Tuple[int, int]], i: typing.Tuple[int, int]):
    if len(cities) == 2:
        return calcDistance(cities[0], cities[1])
    else:
        return 
    
def findRoute(cities: typing.List[typing.Tuple[int, int]]):
    
