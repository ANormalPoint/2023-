import math

# 计算机倒数
def reciprocal(value):
    value = round(float(1) / (float(value)), 10)
    return value


# 计算阶乘
def factorial(value):
    sum = 1
    if value==0 or value==1:
        sum =1
    for i in range(value):
        sum += sum * i
    return sum

# 计算sin
def sin_t(x):
    return round(math.sin(x),10)


# 计算cos
def cos_t(x):
    return round(math.cos(x), 10)


# 计算tan
def tan_t(x):
    return round(math.tan(x), 10)


# 计算csc
def csc_t(x):
    return round(float(1)/math.sin(x), 10)


# 计算sec
def sec_t(x):
    return round(float(1)/math.cos(x), 10)


# 计算lg
def lg_t(x):
    return round(math.log10(x), 10)

# 计算ln
def ln_t(x):
    return round(math.log(x, math.e), 10)
