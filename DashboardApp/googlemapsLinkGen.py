def genGoogleMapsLink(latlon):
    lat = latlon.split(',')[0]
    lon = latlon.split(',')[1]
    url = 'https://maps.google.com/?q='+ lat + ',' + lon
    return url


def genGoogleMapsDirections(latlon1, latlon2):
    lat1 = latlon1.split(',')[0]
    lon1 = latlon1.split(',')[1]
    lat2 = latlon2.split(',')[0]
    lon2 = latlon2.split(',')[1]
    url = 'https://www.google.com/maps/dir/?api=1&origin='+ lat1 + ',' + lon1 + '&destination=' + lat2 + ',' + lon2
    return url
