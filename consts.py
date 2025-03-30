PATH = 'arduino_src/epd2in9/imagedata.cpp'

PRE_HEX = '#include "imagedata.h"\n#include <avr/pgmspace.h>\n\nconst unsigned char IMAGE_DATA[] PROGMEM = {'
POST_HEX = '};\n'

RES_X = 128
RES_Y = 296
