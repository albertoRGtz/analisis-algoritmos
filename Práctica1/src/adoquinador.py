

def get_cuad(esq, rango, esp, tam):
    """
    Obtiene el cuadrante donde está el cuadro especial
    llamando a los cuadrantes de la siguiente forma:
    | 2 | 1 |
    | 3 | 0 |
    :param esq: esquina en la que comienza el cuadro.
    :param rango: número de cuadros por lado.
    :param esp: coordenadas del cuadro especial.
    :param tam: tamaño de cada cuadrado.
    :return: el cuadrante correspondiente.
    """
    if esp[0] < (esq[0] + (rango // 2) * tam):
        if esp[1] < (esq[1] + (rango // 2) * tam):
            return 2
        else:
            return 3
    elif esp[1] < (esq[1] + (rango // 2) * tam):
        return 1
    else:
        return 0


def rot_punto(esq, rango, punto, tam):
    """
    Calcula la ubicación del punto dado después de hacer una rotación
    de 90 grados positiva con centro en el centro del cuadro dado.
    :param esq: esquina en la que comienza el cuadro.
    :param rango: número de cuadritos por lado.
    :param punto: que se rotará.
    :param tam: tamaño de cada cuadrito.
    :return: las coordenadas del punto rotado.
    """
    rot_x = esq[0] + punto[1] - esq[1]
    rot_y = esq[1] + esq[0] + rango * tam - punto[0]
    return rot_x, rot_y


def get_adoqs_cuad(esq, rango, cuad, tam):
    """
    Obtiene los adoquines del cuadrante dado suponiendo que el cuadradito
    especial es que toca el centro del cuadrado dado.
    :param esq: esquina donde comienza el cuadro.
    :param rango: número de cuadritos por lado.
    :param cuad: cuadrante que se calculará.
    :param tam: tamaño de cada cuadrito.
    :return: una lista con los adoquines correspondientes,
    -1 si se le da un cuadrante no válido.
    """
    centro_x = esq[0] + (rango // 2) * tam
    centro_y = esq[1] + (rango // 2) * tam
    if cuad == 0:
        return get_adoqs((centro_x, centro_y), rango // 2,
                         (centro_x, centro_y), tam)
    elif cuad == 1:
        return get_adoqs((centro_x, esq[1]), rango // 2,
                         (centro_x, centro_y - tam), tam)
    elif cuad == 2:
        return get_adoqs(esq, rango // 2,
                         (centro_x - tam, centro_y - tam), tam)
    elif cuad == 3:
        return get_adoqs((esq[0], centro_y), rango // 2,
                         (centro_x - tam, centro_y), tam)
    else:
        return -1


def get_adoqs(esq, rango, esp, tam):
    """
    Adoquina el cuadrado cuya esquina superior izquierda es esq, tiene
    rango cuadritos por cada lado tomando a esp como el cuadradito
    especial y suponiendo que cada cuadrito es de tamaño tam.
    :param esq: esquina donde comienza el cuadrado.
    :param rango: número de cuadritos por lado del cuadrado.
    :param esp: cuadradito especial.
    :param tam: tamaño de cada cuadrito.
    :return: una lista con los adoquines correspondientes.
    """
    num_rot = get_cuad(esq, rango, esp, tam)
    if rango == 2:
        adoq = [(esq[0] + 1, esq[1] + 1),
                (esq[0] + (2 * tam) - 1, esq[1] + 1),
                (esq[0] + (2 * tam) - 1, esq[1] + tam - 1),
                (esq[0] + tam - 1, esq[1] + tam - 1),
                (esq[0] + tam - 1, esq[1] + (2 * tam) - 1),
                (esq[0] + 1, esq[1] + (2 * tam) - 1)]
        for i in range(6):
            for j in range(num_rot):
                adoq[i] = rot_punto(esq, rango, adoq[i], tam)
        return [adoq]
    else:
        centro_x = esq[0] + (rango // 2) * tam
        centro_y = esq[1] + (rango // 2) * tam
        central = [(centro_x - 1, centro_y - 1),
                   (centro_x - 1, centro_y + tam - 1),
                   (centro_x - tam + 1, centro_y + tam - 1),
                   (centro_x - tam + 1, centro_y - tam + 1),
                   (centro_x + tam - 1, centro_y - tam + 1),
                   (centro_x + tam - 1, centro_y - 1)]
        for i in range(6):
            for j in range(num_rot):
                central[i] = rot_punto(esq, rango, central[i], tam)
        adoquines = []
        for i in range(4):
            if i != num_rot:
                adoquines += get_adoqs_cuad(esq, rango, i, tam)
        adoquines.append(central)
        if num_rot == 0:
            adoquines += get_adoqs((centro_x, centro_y), rango // 2, esp, tam)
        elif num_rot == 1:
            adoquines += get_adoqs((centro_x, esq[1]), rango // 2, esp, tam)
        elif num_rot == 2:
            adoquines += get_adoqs(esq, rango // 2, esp, tam)
        else:
            adoquines += get_adoqs((esq[0], centro_y), rango // 2, esp, tam)
        return adoquines
