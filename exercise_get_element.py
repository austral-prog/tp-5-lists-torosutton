def get_element(lista, indice):
    if (indice < 0 and indice<(len(lista)*-1)) or indice > len(lista) or lista==[]:return None
    else :return lista[indice]