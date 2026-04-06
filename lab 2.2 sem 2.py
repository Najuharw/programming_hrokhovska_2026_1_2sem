import math


def min_square(N, W, H):
    left = math.isqrt(N * W * H)
    right = max(W, H) * math.ceil(math.sqrt(N))

    iterations = 0

    while left < right:
        iterations += 1
        mid = (left + right) // 2

        if (mid // W) * (mid // H) >= N:
            right = mid
        else:
            left = mid + 1

    print("iterations:", iterations)
    print("left:", left, "right:", right)

    return left


# Твої тести
print(min_square(10, 2, 3))
print(min_square(2, 1000000000, 999999999))
print(min_square(4, 1, 1))