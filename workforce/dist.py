from math import sin, cos, sqrt, atan2

def getdistance(latlang1,latlang2):
    R = 6373.0
    lat1 = float(latlang1['lat'])
    lon1 = float(latlang1['lng'])
    lat2 = float(latlang2['lat'])
    lon2 = float(latlang2['lng'])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    return distance
