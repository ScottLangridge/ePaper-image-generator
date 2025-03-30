import numpy as np
from PIL import Image, ImageOps

import consts


def convert_image(path, black_bars=False):
    img = Image.open(path)
    if (img.size[0] > img.size[1]):
        img = img.rotate(90, expand=1)

    if black_bars:
        img = ImageOps.pad(img, (consts.RES_X, consts.RES_Y))
    else:
        img = ImageOps.fit(img, (consts.RES_X, consts.RES_Y))

    img = img.convert('1')
    return img


def write_imagedata_cpp(img_hex):
    with open(consts.PATH, 'w') as f:
        f.write(consts.PRE_HEX + img_hex + consts.POST_HEX)


def img_to_hex(img, preview=False):
    assert img.size == (consts.RES_X, consts.RES_Y), f'img_to_hex: Image must be {consts.RES_X}x{consts.RES_Y}px'
    assert img == img.convert('1'), 'img_to_hex: Image must be pure black and white'

    if preview:
        img.show()

    matrix = np.array(img, dtype=int)
    matrix = np.rot90(matrix, 2)
    matrix = matrix.reshape(consts.RES_X, consts.RES_Y // 8, 8)

    out = ''
    for row in matrix:
        for byte in row:
            out += str(hex(int(''.join(map(str, byte)), 2))) + ','

    return out


img = convert_image('imgs/tower_bridge.png', black_bars=False)
hex = img_to_hex(img)
write_imagedata_cpp(hex)
