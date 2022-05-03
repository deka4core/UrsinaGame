from math import floor

import numpy as np
from PIL import Image
from perlin_noise import PerlinNoise

from config import HEIGHTMAP_FILENAME, TEXTUREMAP_FILENAME


def make_maps(noise: PerlinNoise, freq: tuple):
    """
        Создание карты высот и текстур.
    :param noise: Шум Перлина с несколькими октавами.
    :param freq: Точность взятия высот из шума. (по x, по y)
    :return: Создает изображения с картой высот и текстурами карты в папке ./textures/map
    """
    image_size = freq
    xpix, ypix = image_size

    # Создание двух трехмерных массивов, хранящих информацию о картинках.
    height_array = np.zeros([ypix, xpix, 3], dtype=np.uint8)
    tm_array = np.zeros([ypix, xpix, 3], dtype=np.uint8)

    # Перебираем пиксели в шуме Перлина и преобразовываем высоты на карту высот, параллельно создавая текстуры.
    for x in range(xpix):
        for y in range(ypix):

            # Высота. Добавляем 1, чтобы избавиться от отрицательных значений. Умножаем на 127, чтобы получить
            # необходимое значение цвета для карты высот.
            height = floor((noise([x / xpix, y / ypix]) + 1) * 127)

            # Избегаем каких либо ошибок.
            if height > 0:

                # Записываем цвет пикселя в массив, учитывая его высоту.
                if height in range(107):
                    tm_array[y, x] = [201, 174, 116]  # sand
                elif height in range(107, 147):
                    tm_array[y, x] = [65, 156, 3]  # grass
                elif height in range(147, 177):
                    tm_array[y, x] = [94, 108, 98]   # mountain
                else:
                    tm_array[y, x] = [238, 233, 233]  # snow

                height_array[y, x] = [height] * 3  # Сохраняем значение высоты в массив изображения высот.

    # Преобразование массивов в изображения. Затем сохраняем полученные карты.
    heightmap = Image.fromarray(height_array)
    texture_map = Image.fromarray(tm_array)
    heightmap.save(HEIGHTMAP_FILENAME)
    texture_map.save(TEXTUREMAP_FILENAME)