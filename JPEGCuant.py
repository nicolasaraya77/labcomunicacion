import cv2
import numpy as np
import scipy.fftpack as fttp
import time 
ant_16 = lambda x: x >> 4 << 4
cuant = lambda: np.arange(4, 20) * np.arange(4, 20).reshape((-1, 1))

def codif_cuant(src):
    return (src / quant().reshape((1, 16, 1, 16, 1))).astype(np.int8)

def decodif_cuant(src):
    return src * quant().reshape((1, 16, 1, 16, 1)).astype(float)


def decode_dct(src):
    return fftpack.idctn(src, axes=[1,3], norm='ortho'
    ).reshape((
        src.shape[0]*16,
        src.shape[2]*16,
        3
    ))

def encode_dct(src):
    new_shape = (
        prev_16(src.shape[0]),
        prev_16(src.shape[1]),
        3
    )
    new = src[
        :new_shape[0],
        :new_shape[1]
    ].reshape((
        new_shape[0] // 16,
        16,
        new_shape[1] // 16,
        16,
        3
    ))
    return fftpack.dctn(new, axes=[1,3], norm='ortho')



if __name__ == '__main__':
    im = cv2.imread("IMG_0108.JPG")
    enc = encode_dct(im)
    encq = encode_quant(enc)
    decq = decode_quant(encq)
    dec = decode_dct(decq)
    plt.imshow(dec.astype(np.uint8))
    plt.show()
    cv2.imwrite("IMG_0108_recompressed.png", dec.astype(np.uint8))
