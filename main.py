import sympy as sym
from sympy.abc import x
import numpy as np

def func(val):
    fun = sym.poly(x**2 + 2 * x + 3)
    return fun.subs(x, val)

def func_gradient(val):
    fun = sym.poly(x**2 + 2 * x + 3).as_expr()
    diff = sym.diff(fun, x)
    return diff.subs(x, val), diff

def gradient_descent(init_point, lr_rate=1e-2, epsilon=1e-5):
    cnt = 0
    val = init_point
    diff, _ = func_gradient(val)
    while np.abs(diff) > epsilon:
        val = val - lr_rate * diff
        diff, _ = func_gradient(val)
        cnt += 1
    return val, cnt

# 사용 예시
final_val, iterations = gradient_descent(init_point=np.random.uniform(-2, 2))
print(f"최종 값: {final_val}, 반복 횟수: {iterations}")
