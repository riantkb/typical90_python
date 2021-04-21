def main():
    _, l = map(int, input().split())
    k = int(input())
    a = list(map(int, input().split()))
    a.append(l)

    ok, ng = 0, l + 1
    while ok + 1 < ng:
        mid = (ok + ng) // 2
        cnt = 0
        prv = 0
        for p in a:
            if p - prv >= mid:
                cnt += 1
                prv = p

        if cnt >= k + 1:
            ok = mid
        else:
            ng = mid

    print(ok)


if __name__ == "__main__":
    main()
