"""
    MAP CONFIG
"""
from random import randint

from ursina import rgb

PERLIN_NOISE_OCTAVES = 6
PERLIN_NOISE_SEED = randint(0, 999)
PERLIN_NOISE_FREQUENCY = (500, 500)  # (x, y)

HEIGHTMAP_FILENAME = './textures/map/heightmap.png'
TEXTUREMAP_FILENAME = './textures/map/texturemap.png'

WATER_PLANE_SCALE = 20
WATER_PLANE_COLOR = rgb(14, 135, 204)