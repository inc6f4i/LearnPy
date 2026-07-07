#260707_day072_01_.py
# ── 퍼셉트론 직접 구현 ──




def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 입력값
x = np.array([2.0, 3.0])
w = np.array([0.5, -1.0])
b = 1.0

# 단계별 계산
products = w * x          # ① 각각 곱하기
weighted_sum = np.sum(products)  # ② 가중합
z = weighted_sum + b      # ③ 편향 더하기
a = sigmoid(z)            # ④ 활성화

print('=' * 40)
print(f'① 곱하기:   w·x = {products}')
print(f'② 가중합:   Σ   = {weighted_sum}')
print(f'③ 편향추가: z   = {z}')
print(f'④ 활성화:   a   = {a:.4f}')
print('=' * 40)