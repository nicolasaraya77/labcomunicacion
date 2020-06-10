import cv2
import numpy as np
import scipy.fftpack as fttp
import time 
ant_16 = lambda x: x >> 4 << 4

def comp_tcd (src):
    nueva_forma =(
        ant_16(src.shape[0]),
        ant_16(src.shape[1]),
        3
    )
    new = src[

    ].shape((
        nueva_forma[0] // 16,
        16,
        nueva_forma[1] // 16,
        16,
        3
    ))
    return fttp.dctn(new, axes = [1,3], norm ='ortho')

def decomp_tcd (src):
    return fttp.idctn(src, axes=[1,3], norm='ortho'
                      ).reshape((
                          src.shape[0]*16,
                          src.shape[2]*16,
                          3
                          ))

if __name__ == '__main__':
    im = cv2.imread()
    enc = encode_dct(im)
    dec = decode_dct(enc)
    cv2.imwrite("IMG_0108_recompressed.png", dec.astype(np.uint8))
