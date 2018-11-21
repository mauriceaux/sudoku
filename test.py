from generador import Sudoku
import numpy as np


"""s      = [9,1,0,0,3,0,0,0,0]
s.append([0,0,0,0,0,4,0,0,0])
s.append([0,0,8,0,0,0,5,0,1])
s.append([0,0,0,0,0,0,4,0,6])
s.append([0,0,0,0,0,0,4,0,6])"""
sudoku = Sudoku()
sudoku.insertarNumero(0,0,1)
sudoku.insertarNumero(0,4,2)

sudoku.insertarNumero(1,2,2)
sudoku.insertarNumero(1,8,6)

sudoku.insertarNumero(2,2,8)
sudoku.insertarNumero(2,3,9)
sudoku.insertarNumero(2,5,4)

sudoku.insertarNumero(3,0,4)
sudoku.insertarNumero(3,1,8)
sudoku.insertarNumero(3,2,5)
sudoku.insertarNumero(3,5,7)

sudoku.insertarNumero(4,2,7)
sudoku.insertarNumero(4,4,5)
sudoku.insertarNumero(4,7,9)

sudoku.insertarNumero(5,4,3)
sudoku.insertarNumero(5,6,4)

sudoku.insertarNumero(6,0,8)
sudoku.insertarNumero(6,4,4)
sudoku.insertarNumero(6,5,6)

#sudoku.insertarNumero(7,0,3)
sudoku.insertarNumero(7,6,5)

sudoku.insertarNumero(8,3,5)
#sudoku.insertarNumero(8,5,3)
#sudoku.insertarNumero(8,7,4)

if not sudoku.validarSudoku():
    print("sudoku no valido!")
    exit()

duda = []

while not sudoku.resuelto:
    if not sudoku.validarSudoku():
        movDuda = duda.pop()
        while sudoku.movActual > movDuda[0]:
            sudoku.deshacer()
        sudoku.candidatosDescartados.append([movDuda[1], movDuda[2], movDuda[3]])
        i, = np.where(sudoku.candidatos[0][2] == movDuda[3])
        #print("indice {}".format(i))
        
        sudoku.candidatos[0][2] = np.delete(sudoku.candidatos[0][2],i)
        #print("me devolvi al error -> {}, candidatos {}".format(movDuda, sudoku.candidatos[0]))
        #exit()
    candidato = sudoku.candidatos[0]
    if len(candidato[2]) < 1:
        print("sin candidatos! movimiento {}".format(sudoku.movActual))
        print("no pude resolver :(")
        exit()
    if len(candidato[2]) > 1:
        duda.append([sudoku.movActual, candidato[0], candidato[1], candidato[2][0]])
    sudoku.insertarNumero(candidato[0], candidato[1], candidato[2][0])
    print(len(sudoku.candidatos))


print("resuelto!")
print(sudoku.sudoku)
exit()

#print(sudoku.obtenerCandidatos(8,8))
print(sudoku.candidatos)
print(sudoku.valido)
print(sudoku.resuelto)
