def condicionalesLetras(dedos):
    letras = {
        (1, 1, 0, 0, 0, 0): "A", # ok
        (0, 0, 1, 1, 1, 1): "B", # ok
        (0, 1, 1, 1, 1, 1): "C", # ok
        (0, 0, 0, 0, 0, 1): "D", # ok
        (0, 0, 0, 0, 0, 0): "E", # ok
        (0, 0, 1, 1, 1, 0): "F", # ok
        (0, 0, 0, 0, 1, 0): "G", # Revisar
        (0, 0, 1, 0, 0, 0): "I", # ok
        (1, 1, 0, 0, 1, 1): "K", # ok
        (1, 1, 0, 0, 0, 1): "L", # ok
        (0, 1, 0, 0, 1, 1): "N", # ok
        (0, 1, 0, 1, 1, 1): "M", # ok
        (1, 0, 0, 0, 0, 1): "O", # ok
        (0, 0, 0, 1, 1, 0): "P", # OK
        #(0, 1, 1, 1, 1, 1): "Q", # Revisar
        (0, 0, 1, 0, 1, 0): "R", # ok
        (0, 1, 0, 0, 0, 0): "S", # OK 
        (0, 1, 0, 0, 0, 1): "T", # ok
        (0, 0, 1, 0, 0, 1): "U", # ok 
        (0, 0, 0, 0, 1, 1): "V", # ok
        (0, 0, 0, 1, 1, 1): "W", # ok
        #(1, 0, 0, 1, 0, 0): "X", # Revisar
        (1, 1, 1, 0, 0, 0): "Y", # ok
        #(0, 0, 1, 0, 1, 0): "Z", # Revisar
        (1, 1, 1, 1, 1, 1): " ",
        
    }
    return letras.get(dedos, dedos)