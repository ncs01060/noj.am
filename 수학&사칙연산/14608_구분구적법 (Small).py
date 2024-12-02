def polynomial(x, coeffs):
    return sum(c * x ** i for i, c in enumerate(reversed(coeffs)))


# 정확한 적분값 계산
def exact_integral(coeffs, a, b):
    integral_value = 0
    for i, c in enumerate(reversed(coeffs)):
        integral_value += c / (i + 1) * (b ** (i + 1) - a ** (i + 1))
    return integral_value


# 구분구적법을 이용한 근사 적분 계산
def approximate_integral(coeffs, a, b, n, epsilon):
    delta_x = (b - a) / n
    sum_result = 0
    for k in range(n):
        x_k = a + k * delta_x + epsilon
        sum_result += polynomial(x_k, coeffs) * delta_x
    return sum_result

K = int(input())
coeffs = list(map(int, input().split()))
a, b, N = map(int, input().split())

exact_value = exact_integral(coeffs, a, b)

low, high = 0, (b - a) / N
epsilon = -1
tolerance = 1e-4

while high - low > tolerance:
    mid = (low + high) / 2
    approx_value = approximate_integral(coeffs, a, b, N, mid)
    error = abs(approx_value - exact_value)

    if error < tolerance:
        epsilon = mid
        break
    elif approx_value < exact_value:
        low = mid
    else:
        high = mid

if epsilon == -1:
    print(-1)
else:
    print(f"{epsilon:.4f}")