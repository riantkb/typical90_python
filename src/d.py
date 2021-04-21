def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    rows = [sum(x) for x in a]
    cols = [sum(x[j] for x in a) for j in range(w)]
    print(*(' '.join(str(rows[i] + cols[j] - a[i][j])
                     for j in range(w)) for i in range(h)), sep='\n')


if __name__ == "__main__":
    main()
