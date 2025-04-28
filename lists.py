def remove_elements(lst):
    # Eliminamos primer, quinto y sexto elemento si existen
    indices = [0, 4, 5]
    # Para no alterar la lista mientras la recorremos, lo hacemos en orden inverso
    for i in sorted(indices, reverse=True):
        if i < len(lst):
            del lst[i]
    return lst

def add_elements(lst):
    # Agregamos 'Pink' al principio y 'Yellow' al final
    lst.insert(0, 'Pink')
    lst.append('Yellow')
    return lst

def is_empty(lst):
    # Devuelve True si está vacía
    return len(lst) == 0

def check_lists(lst1, lst2):
    # Verificamos que ambas tengan al menos 3 elementos
    if len(lst1) >= 3 and len(lst2) >= 3:
        return lst1[2] == lst2[2]
    else:
        return False

def list_of_lists(lists):
    # Modificamos cada sublista según las instrucciones
    result = []
    if len(lists) >= 1:
        result.append(lists[0][:2])
    if len(lists) >= 2:
        result.append(lists[1][1:4])
    if len(lists) >= 3:
        result.append(lists[2][-2:])
    return result
