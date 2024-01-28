def is_valid_move(maze, x, y, visited):
    rows = len(maze)
    cols = len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0 and not visited[x][y]

def solve_maze(maze):
    rows = len(maze)
    cols = len(maze[0])

    # Inisialisasi matriks visited
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # Mulai dari titik awal (0, 0)
    start = (0, 0)
    end = (rows - 1, cols - 1)

    # Panggil fungsi rekursif untuk menemukan jalan keluar
    if find_path(maze, start[0], start[1], end[0], end[1], visited):
        print("Jalan keluar ditemukan:")
        print_solution(maze, visited)
    else:
        print("Tidak ada jalan keluar.")

def find_path(maze, x, y, end_x, end_y, visited):
    # Basis: Jika mencapai tujuan
    if x == end_x and y == end_y:
        visited[x][y] = True
        return True

    # Periksa apakah langkah saat ini valid
    if is_valid_move(maze, x, y, visited):
        # Tandai sel saat ini sebagai sudah dikunjungi
        visited[x][y] = True

        # Coba semua langkah yang mungkin
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # gerak ke arah kanan, bawah, kiri, atas
        for move in moves:
            new_x, new_y = x + move[0], y + move[1]
            if find_path(maze, new_x, new_y, end_x, end_y, visited):
                return True

        # Jika tidak ada langkah yang berhasil, tandai sel ini sebagai tidak dikunjungi
        visited[x][y] = False

    return False

def print_solution(maze, visited):
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if visited[i][j]:
                print("x", end=" ")  # Rute solusi
            elif maze[i][j] == 1:
                print("1", end=" ")  # Tembok
            else:
                print("0", end=" ")  # Jalan
        print()

# Contoh labirin (0 = jalan, 1 = tembok)
maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

solve_maze(maze)
