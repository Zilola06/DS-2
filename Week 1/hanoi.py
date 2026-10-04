def hanoi(n, src, dst, via):
    if n == 1:
        print(f"disk 1: {src} -> {dst}")
        return
    hanoi(n - 1, src, via, dst)
    print(f"disk {n}: {src} -> {dst}")
    hanoi(n - 1, via, dst, src)

hanoi (3, 'A', 'C', 'B')
