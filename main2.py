def mach_coor(json_response):

    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    toponym_size = toponym["boundedBy"]["Envelope"]['lowerCorner']
    toponym_size2 = toponym["boundedBy"]["Envelope"]['upperCorner']
    toponym_lowerCorner1, toponym_lowerCorner2 = toponym_size.split(" ")
    toponym_upperCorner1, toponym_upperCorner2 = toponym_size2.split(" ")

    spn1 = abs(float(toponym_lowerCorner1) - float(toponym_upperCorner1)) / 2.0
    spn2 = abs(float(toponym_lowerCorner2) - float(toponym_upperCorner2)) / 2.0

    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([str(spn1), str(spn2)]),
        "l": "map",
        "pt": ",".join([toponym_longitude, toponym_lattitude, 'pm2rdm'])
    }

    return map_params