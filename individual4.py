import math
if __name__ == '__main__':
 
    x = float (input ('Enter x: '))
    sum_, eps = 0, 1e-10
    y = 0.57721566490153286
    n= 1
    while True:
        prev_sum = sum_
        sum_ += (x**(2*n)) / (2*n * math.factorial(2*n))
        n += 1
        if math.fabs(sum_ - prev_sum) < eps:
            break

    print(f'Chi({x}) = {y + math.log(x) + sum_}')