import sys
import pygame
import time
from adoquinador import get_adoqs


def main():
    """
    Ejecuta la interfaz de usuario del programa. Su uso se
    especifica en el README.
    """
    pygame.init()

    'Colores'
    col_bg = 75, 115, 255
    col_esp = 105, 45, 170
    col_adoq = 250, 100, 50
    col_lin = 255, 255, 255

    'Creación de la pantalla.'
    size = 513
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption('Adoquinador')
    screen.fill(col_bg)

    while True:
        'Para elegir el tamaño de la cuadrícula.'
        if len(sys.argv) > 1:
            k = int(sys.argv.pop(1))
        else:
            'Pantalla de bienvenida'
            fuente1 = pygame.font.Font('freesansbold.ttf', 64)
            wm = fuente1.render(' !Bienvenido! ', True, col_adoq, col_esp)
            wm_rect = wm.get_rect()
            wm_rect.center = (size // 2, size // 3)

            fuente2 = pygame.font.Font('freesansbold.ttf', 16)
            ins = fuente2.render(' Para comenzar elige un tamaño \'k\' ' +
                                 'con el teclado ', True, col_adoq, col_esp)
            ins_rect = ins.get_rect()
            ins_rect.center = (size // 2, size // 2)

            k = None
            while k is None:
                screen.fill(col_bg)
                screen.blit(wm, wm_rect)
                screen.blit(ins, ins_rect)
                for evento in pygame.event.get():
                    if evento.type == pygame.KEYDOWN:
                        k = int(pygame.key.name(evento.key))
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                pygame.display.update()

        'Número de celdas por lado del cuadrado.'
        m = 2 ** k
        screen.fill(col_bg)

        'Dibuja la cuadrícula inicial.'
        tam = (size - 1) / m
        for i in range(m):
            pygame.draw.line(screen, col_lin, (i * tam, 0), (i * tam, size), 1)
            pygame.draw.line(screen, col_lin, (0, i * tam), (size, i * tam), 1)
        pygame.draw.line(screen, col_lin, (size - 1, 0), (size - 1, size), 1)
        pygame.draw.line(screen, col_lin, (0, size - 1), (size, size - 1), 1)

        'Para elegir la celda especial con el mouse.'
        esp = None
        while esp is None:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if sum(pygame.mouse.get_pressed(3)) > 0:
                pos_x, pos_y = pygame.mouse.get_pos()
                pos_x = pos_x - (pos_x % tam)
                pos_y = pos_y - (pos_y % tam)
                sqr = [(pos_x + 1, pos_y + 1),
                       (pos_x + tam - 1, pos_y + 1),
                       (pos_x + tam - 1, pos_y + tam - 1),
                       (pos_x + 1, pos_y + tam - 1)]
                pygame.draw.polygon(screen, col_esp, sqr, 0)
                esp = (pos_x, pos_y)
            pygame.display.flip()

        'Obtiene los adoquines para el cuadrito seleccionado.'
        adoquines = get_adoqs((0, 0), m, esp, tam)

        'Segundos para que la ejec dure 10s.'
        secs = 30 / (m * m)

        'Dibuja los polígonos que fueron calculados.'
        for adoquin in adoquines:
            pygame.draw.polygon(screen, col_adoq, adoquin, 0)
            pygame.display.flip()
            time.sleep(secs)

        'Para mantener abierto el programa.'
        keep_open = True
        while keep_open:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if sum(pygame.mouse.get_pressed(3)) > 0:
                    keep_open = False


if __name__ == '__main__':
    main()
