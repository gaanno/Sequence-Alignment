from needleman import NW


if __name__ == "__main__":
    seq1 = input("Ingrese secuencia 1: ")
    seq2 = input("Ingrese secuencia 2: ")
    match = int(input("Ingrese valor coincidencia: "))
    mismatch = int(input("Ingrese costo falta de coincidencia: "))
    gap = int(input("Ingrese gap: "))
    costo_extension = int(input("Ingrese costo extension: "))


    NW(seq1, seq2, match, mismatch, gap,costo_extension)