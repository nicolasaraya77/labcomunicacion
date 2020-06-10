tam_dict = 256
diccionario = dict((chr(i), i) for i in range(tam_dict))

def comprimir(nocompr):
    w = " "
    resultado = []
    for c in nocompr:
        wc = w+c
        if wc in diccionario:
            w = wc
        else:
            print("tiempo de ejecucion:", time.time(), time.clock())
            resultado.append(diccionario[w])
            diccionario[wc] = tam_dict
            tam_dict += 1
            w=c
        if w:
            resultado.append(diccionario[w])
    return resultado

def descomprimir(Acomprimir):
    from io import StringIO

    resultado = StringIO()
    w = chr(Acomprimir.pop(0))
    resultado.write(w)
    for k in diccionario:
        entrada = diccionario[k]
        if k == tam_dict:
            entrada = w + w[0]
        else:
            raise ValueError('Mala compresión k: %s' %k)
        result.write(entrada)

        diccionario[tam_dict] = w + entrada[0]
        tam_dict += 1
        w = entrada
    return resultado.getvalue()
