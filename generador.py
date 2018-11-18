#genera archivo numpy con pasos random para llenar una matriz de 3x3 con las reglas del sudoku
import numpy as np
import collections
import random

class Sudoku:
    def __init__(self, sudoku = None):
        self.sudoku = sudoku
        if self.sudoku is None or type(self.sudoku) is not np.ndarray or self.sudoku.shape[0] != 9 or self.sudoku.shape[1] != 9:
            print("Creando sudoku en blanco")
            self.sudoku = np.zeros((9,9))
        else:
            print("Usando sudoku suministrado")
        self.candidatos = []
        self.resuelto = False
        self.valido = self.validarCandidatos()
        self.historialMovimientos = []
        self.movActual = -1


    def insertarNumero(self,i, j, num):
        self.movActual = self.movActual + 1
        if self.movActual >= 0 and self.movActual < len(self.historialMovimientos):
            self.historialMovimientos[self.movActual] = [i,j,num]
        else:
            self.historialMovimientos.append([i,j,num])
        
        
        self.sudoku[i][j] = num

        self.validarSudoku()
        if len(self.candidatos) == 0 and self.valido:
            self.resuelto = True
        else:
            self.resuelto = False

    def obtenerCoordMinCuadrante(self, i, j):
        min = 0
        if i < 3:
            min = 0
        elif i >= 3 and i < 6:
            min = 3
        else: min = 6
        minX = min

        if j < 3:
            min = 0
        elif j >= 3 and j < 6:
            min = 3
        else: min = 6
        minY = min
        return minX, minY

    def validarSudoku(self):
        for i in range(9):
            for j in range(9):
                num = self.sudoku[i][j]
                if num == 0: continue
                fila = self.sudoku[i, :]
                columna = self.sudoku[:, j]

                minX, minY = self.obtenerCoordMinCuadrante(i,j)
                
                cuadrante = self.sudoku[minX:minX+3, minY:minY+3].reshape(9)
                if np.count_nonzero(fila == num) > 1 or np.count_nonzero(columna == num) > 1 or np.count_nonzero(cuadrante == num) > 1:
                    self.valido = False
                    self.resuelto = False
                    return self.valido
        self.valido = True and self.validarCandidatos()
        return self.valido

    def validarCandidatos(self):
        self.calcularCandidatos()
        if len(self.candidatos) > 0 and self.candidatos[0][2].size < 1:
            return False
        return True
            

    def obtenerCandidatos(self, i,j):
        candidatos = np.asarray(range(1,10))
        minX, minY = self.obtenerCoordMinCuadrante(i,j)
        fila = self.sudoku[i, :]
        columna = self.sudoku[:, j]
        cuadrante = self.sudoku[minX:minX+3, minY:minY+3].reshape(9)
        candidatos = np.setdiff1d(candidatos, fila)        
        candidatos = np.setdiff1d(candidatos, columna)
        candidatos = np.setdiff1d(candidatos, cuadrante)
        return candidatos
    
    def calcularCandidatos(self):
        self.candidatos = []
        for i in range(9):
            for j in range(9):
                if self.sudoku[i][j] == 0:
                    arr = [i,j]
                    arr.append(self.obtenerCandidatos(i,j))
                    self.candidatos.append(arr)
        self.obtenerUnicoEnCuadrantes()
        self.candidatos = sorted(self.candidatos, key=lambda x:x[2].size, reverse=False)

    def obtenerCandidatosCuadrante(self,i):
        retorno = []
        idx = 0
        for candidato in self.candidatos:
            if i == 0:
                if 0 <= candidato[0] <= 2 and 0 <= candidato[1] <= 2:
                    retorno.append(idx)
            if i == 1:
                if 0 <= candidato[0] <= 2 and 3 <= candidato[1] <= 5:
                    retorno.append(idx)
            if i == 2:
                if 0 <= candidato[0] <= 2 and 6 <= candidato[1] <= 8:
                    retorno.append(idx)
            if i == 3:
                if 3 <= candidato[0] <= 5 and 0 <= candidato[1] <= 2:
                    retorno.append(idx)
            if i == 4:
                if 3 <= candidato[0] <= 5 and 3 <= candidato[1] <= 5:
                    retorno.append(idx)
            if i == 5:
                if 3 <= candidato[0] <= 5 and 6 <= candidato[1] <= 8:
                    retorno.append(idx)
            if i == 6:
                if 6 <= candidato[0] <= 8 and 3 <= candidato[1] <= 2:
                    retorno.append(idx)
            if i == 7:
                if 6 <= candidato[0] <= 8 and 3 <= candidato[1] <= 5:
                    retorno.append(idx)
            if i == 8:
                if 6 <= candidato[0] <= 8 and 3 <= candidato[1] <= 8:
                    retorno.append(idx)
            idx = idx+1
        return retorno

        

    def obtenerUnicoEnCuadrantes(self):
        for i in range(9):
            #obtengo indices de candidatos
            idxCandidatosCuadrante = self.obtenerCandidatosCuadrante(i)
            print("************************************")
            print("candidatos de 8,8")
            for idx in idxCandidatosCuadrante:
                print(self.candidatos[idx])
            print("************************************")
            #exit()
            for idx in idxCandidatosCuadrante:

                unique, counts = np.unique(self.candidatos[idx][2], return_counts=True)
                cont = 0
                for conteo in counts:
                    if conteo == 1:
                        self.candidatos[idx][2] = unique[cont]
                    cont = cont+1
                #counter = collections.Counter(a)

                #for numCandidato in self.candidatos[idx][2]:
                #    ocurerncias = np.isin(numCandidato, candidatosCuadrante)
                    
                    


            #encontrar numero unico entre candidatos
            #retornar candidato
            #retorno.append(self.candidatos[idxUnico])
        #return retorno
            


    def deshacer(self):
        if(self.movActual < 0):
            return
        
        #print("hoooooooooooooola! \n{}".format(self.sudoku))
        #exit()
        self.sudoku [ self.historialMovimientos[ self.movActual] [0] ][ self.historialMovimientos[ self.movActual] [1] ] = 0
        self.movActual = self.movActual - 1
        self.validarSudoku()
        print("deshacer {}".format(self.movActual))
        

    def rehacer(self):
        #print("tamaño historial {}".format(len(self.historialMovimientos)))
        if(self.movActual +1 >= len(self.historialMovimientos)):
            return
        
        self.movActual = self.movActual + 1
        #print("rehacer {}".format(self.movActual))
        self.sudoku [ self.historialMovimientos[ self.movActual] [0] ][ self.historialMovimientos[ self.movActual] [1] ] = self.historialMovimientos[ self.movActual][2]
        self.validarSudoku()

    def completar(self):
        self.calcularCandidatos()
        
        print("inicio")
        if not self.valido:
            print("sudoku no valido")
            return
        #print("candidatos {}".format(self.candidatos[(len(self.candidatos)-1)]))

        #print("range(len(self.candidatos)-1) {}".format(range(len(self.candidatos)-1)))
        #exit()
        cont = 0
        duda = []
        while not self.resuelto:
            print("movimiento actual {}".format(self.movActual))
            print(self.sudoku)
            if not self.valido:
                print("duda {}".format(duda))
                while duda[-1] <= self.movActual:
                    self.deshacer()
                duda.pop()
                continue
            if 0 == len(self.candidatos):
                continue
            candidato = self.candidatos[0]
            if cont >= candidato[2].size:
                cont = 0
            if candidato[2].size < 1:
                continue
            if candidato[2].size > 1:
                duda.append(sudoku.movActual)
            
            #print("candidato {}".format(candidato))
            #print("cont {}".format(cont))
            #print(len(candidato[2]))
            #print("len(self.historialMovimientos) > self.movActual {} > {}".format(len(self.historialMovimientos), self.movActual))
            if(len(self.historialMovimientos) > self.movActual +1):
                print("eligiendo un nuevo candidato {}".format(candidato[2]))
                #cand = self.obtenerCandidatos(self.historialMovimientos[self.movActual+1][0], self.historialMovimientos[self.movActual+1][1])
                #indx, = np.where(cand == self.historialMovimientos[self.movActual+1][2])
                #indx, = np.where(cand == 6)
                indx, = np.where(candidato[2] == self.historialMovimientos[self.movActual+1][2])
                #print(indx)
                #print(self.sudoku)
                #print(cand)
                print(self.historialMovimientos[self.movActual+1])
                #print(self.historialMovimientos[self.movActual+1][2])
                print("candidato")
                print(candidato)
                #exit()
                #print(self.historialMovimientos[self.movActual-3])
                #print(self.historialMovimientos[self.movActual-2])
                #print(self.historialMovimientos[self.movActual-1])
                
                #print(self.historialMovimientos[self.movActual+1])
                #print(self.historialMovimientos[self.movActual+2])
                #exit()
                if indx+1 >= len(candidato[2]):
                    self.deshacer()
                    continue
                num = candidato[2][indx+1]
            else:
                print("candidato")
                print(candidato)
                #self.obtenerCandidatos()
                num = candidato[0]
            print("insertando en {}, {} el numero {}".format(candidato[0], candidato[1], num))
            #print("candidato[2][{}]".format(cont))
            self.insertarNumero(candidato[0], candidato[1], num)
            cont = cont + 1
        print("fin")



"""s      = [9,1,0,0,3,0,0,0,0]
s.append([0,0,0,0,0,4,0,0,0])
s.append([0,0,8,0,0,0,5,0,1])
s.append([0,0,0,0,0,0,4,0,6])
s.append([0,0,0,0,0,0,4,0,6])"""
sudoku = Sudoku()
sudoku.insertarNumero(0,0,9)
sudoku.insertarNumero(0,1,1)
sudoku.insertarNumero(0,4,3)

sudoku.insertarNumero(1,5,4)

sudoku.insertarNumero(2,2,8)
sudoku.insertarNumero(2,6,5)
sudoku.insertarNumero(2,8,1)

sudoku.insertarNumero(3,6,4)
sudoku.insertarNumero(3,8,6)

sudoku.insertarNumero(4,1,7)
sudoku.insertarNumero(4,7,9)

sudoku.insertarNumero(5,5,8)
sudoku.insertarNumero(5,6,7)
sudoku.insertarNumero(5,7,5)

sudoku.insertarNumero(6,0,7)
sudoku.insertarNumero(6,2,5)
sudoku.insertarNumero(6,6,6)

sudoku.insertarNumero(7,1,3)
sudoku.insertarNumero(7,4,8)
sudoku.insertarNumero(7,7,7)
sudoku.insertarNumero(7,8,9)

sudoku.insertarNumero(8,2,2)
sudoku.insertarNumero(8,3,1)
sudoku.insertarNumero(8,5,6)

print("candidatos 8,8: {}".format(sudoku.obtenerCandidatos(8,8)))
sudoku.obtenerUnicoEnCuadrantes()
for candidato in sudoku.candidatos:
    if candidato[0] == 8 and candidato[1] == 8:
        print("candidatos 8,8 {}".format(candidato[2]))
exit()

sudoku.obtenerUnicoEnCuadrantes()
for candidato in sudoku.candidatos:
    if candidato[0] == 8 and candidato[1] == 8:
        print("candidato[2] {}".format(candidato[2]))
exit()

#noveno cuadrante
#print(sudoku.candidatos)
#exit()
#for i in range(6,9):
#    for j in range(6,9):
#        print(sudoku.obtenerCandidatos(i,j))

#print(sudoku.sudoku)
#print(sudoku.candidatos)
#exit()


sudoku.completar()
print("sudoku resuelto \n{}\n numero de movimientos {}".format(sudoku.sudoku, len(sudoku.historialMovimientos)))
exit()
#print("mov actual {} ".format(sudoku.movActual))
sudoku.insertarNumero(0,0,1)

#print("mov actual {} ".format(sudoku.movActual))
#exit()
sudoku.insertarNumero(0,1,2)
sudoku.insertarNumero(0,2,3)
sudoku.insertarNumero(1,0,4)
"""sudoku.insertarNumero(1,1,5)
sudoku.insertarNumero(1,2,6)
sudoku.insertarNumero(2,0,7)
sudoku.insertarNumero(2,1,8)
sudoku.insertarNumero(2,2,9)"""
#print("historial de movimientos {}".format(sudoku.historialMovimientos))
#sudoku.deshacer()
#print("mov actual {} ".format(sudoku.movActual))
#print("historial de movimientos {}".format(sudoku.historialMovimientos))
#exit()
print("sudoku inicial \n{} movimiento {}".format(sudoku.sudoku, sudoku.movActual))
sudoku.deshacer()
sudoku.deshacer()

sudoku.deshacer()
sudoku.deshacer()
sudoku.rehacer()
sudoku.rehacer()
sudoku.rehacer()
sudoku.rehacer()
print("sudoku final \n{} movimiento {}".format(sudoku.sudoku, sudoku.movActual))
exit()
#sudoku.insertarNumero(2,2,9)
sudoku.insertarNumero(8,2,9)
print("sudoku.resuelto {}".format(sudoku.resuelto))
print("sudoku.valido {}".format(sudoku.valido))

print("historial {}".format(sudoku.historialMovimientos))
#print("candidatos {}".format(sudoku.candidatos))

