#import vector2d
from vector2d import Vector2D #alternatively to import
def Main():
    vec1=Vector2D(5,6)
    vec2=Vector2D(1,1)
    Vec=(vec1, vec2)
    print(Vec[0], Vec[1])

if __name__=="__main__":
    Main()