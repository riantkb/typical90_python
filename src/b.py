def main():
    def rec(rem, lis, dep):
        if dep < 0:
            return
        if rem == 0:
            if dep == 0:
                print(''.join(lis))
        else:
            lis.append('(')
            rec(rem - 1, lis, dep + 1)
            lis[-1] = ')'
            rec(rem - 1, lis, dep - 1)
            lis.pop()

    n = int(input())
    rec(n, [], 0)


if __name__ == "__main__":
    main()
