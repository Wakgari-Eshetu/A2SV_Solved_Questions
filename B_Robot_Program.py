t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    s = input()

    def time_to_zero(start):
        pos = start
        for i in range(n):
            if s[i] == 'L':
                pos -= 1
            else:
                pos += 1
            if pos == 0:
                return i + 1
        return None

   
    first = time_to_zero(x)
    if first is None or first > k:
        print(0)
        continue

    count_zero = 1
    k -= first
    cycle = time_to_zero(0)

    if cycle is not None:
        count_zero += k // cycle

    print(count_zero)