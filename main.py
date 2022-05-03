from perlin_noise import PerlinNoise
from ursina import Ursina, Vec3, Entity, Terrain, EditorCamera, DirectionalLight
from ursina.shaders import lit_with_shadows_shader

from config import PERLIN_NOISE_OCTAVES, PERLIN_NOISE_SEED, PERLIN_NOISE_FREQUENCY, WATER_PLANE_COLOR, \
    WATER_PLANE_SCALE, HEIGHTMAP_FILENAME, TEXTUREMAP_FILENAME
from maps import make_maps

app = Ursina()

# Создание ландшафта.
noise = PerlinNoise(octaves=PERLIN_NOISE_OCTAVES, seed=PERLIN_NOISE_SEED)  # Шум Перлина
make_maps(noise, PERLIN_NOISE_FREQUENCY)
landscape = Terrain(heightmap=HEIGHTMAP_FILENAME, skip=1)
terrain = Entity(model=landscape, scale=(20, 5, 20), texture=TEXTUREMAP_FILENAME,
                 shader=lit_with_shadows_shader)

# Создание воды. Todo: GLSL Shader cartoon water
water_plane = Entity(model='quad', color=WATER_PLANE_COLOR, position=Vec3(0, 1.9, 0),
                     rotation=(90, 0, 0),
                     scale=(WATER_PLANE_SCALE, WATER_PLANE_SCALE, 1), shader=lit_with_shadows_shader)

# Камера.
ec = EditorCamera(rotation_smoothing=10, enabled=1, rotation=(30, 30, 0))

# Свет
DirectionalLight(parent=Entity(), y=2, z=3, shadows=True, rotation=(0, 0, 0))

app.run()
