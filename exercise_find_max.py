def find_max(lista):
    """
    Encuentra y retorna el valor máximo en una lista de números.
    Si la lista está vacía, retorna None.
    Args:
        lista: Una lista de números

    Returns:
        El valor máximo de la lista o None si está vacía
    """
    if lista==[]:
        return None
    elif len(lista)==1:
        return lista[0]
    else:
        return max(lista)