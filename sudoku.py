# Fungsi untuk mengecek apakah angka dapat ditempatkan
def is_valid(board, row, col, num):
    # Cek di baris
    if num in board[row]:
        return False
    
    # Cek di kolom
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Cek di kotak 3x3
    box_row, box_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    
    return True

# Fungsi rekursif untuk menyelesaikan Sudoku
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Cari sel kosong
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Coba isi angka
                        if solve_sudoku(board):  # Rekursi
                            return True
                        board[row][col] = 0  # Backtrack jika gagal
                return False  # Tidak ada angka yang valid
    return True  # Sudoku selesai

# Contoh input Sudoku (0 adalah sel kosong)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Menjalankan solver
solve_sudoku(sudoku_board)

# Menampilkan hasil
for row in sudoku_board:
    print(row)
