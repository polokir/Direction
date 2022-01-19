f=input("facing ")
t=int(input("turn "))



def direction(facing, turn):
    maindirections ={"N":0,"NE":45,"E":90,"SE":135,"S":180,"SW":225,"W":270,"NE":315}
    direct=maindirections[facing]
    direct=(direct+turn)%360    
    if(direct>=0 and direct<45):
        return "N"
    elif(direct>=45 and direct<90):
        return "NE"
    elif(direct>=90 and direct<135):
        return "E"
    elif(direct>=135 and direct<180):
        return "SE"
    elif(direct>=180 and direct<225):
        return "S"
    elif(direct>=225 and direct<270):
        return "SW"
    elif(direct>=270 and direct<315):
        return "W"
    elif(direct>=315 and direct<359):
        return "NW"
    
print(direction(f,t))



        
    