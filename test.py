from generador import Sudoku


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

print(sudoku.sudoku)