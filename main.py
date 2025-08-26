from fractions import Fraction

def main():
    n = int(input("Enter how many numbers the sequence should have: "))
    numbers = []
    for i in range(1, n+1):
        numbers.append(Fraction(input(f"Write a{i}:")))

    factors = [Fraction(0)] * n
    for i in range(n):
        denominator = Fraction(1)
        for j in range(n):
            if j != i:
                denominator *= Fraction(i+1 - (j + 1))

        #polinomial is (x-1)(x-2)...(x-n) without (x-i)
        polynomial = [Fraction(1)]
        for j in range(n):
            if j != i:
                new = [Fraction(0)] * (len(polynomial) + 1)
                for k in range(len(polynomial)):
                    new[k] += polynomial[k] * Fraction(-(j+1))
                    new[k+1] += polynomial[k]
                polynomial = new

        factor = numbers[i] / denominator
        for k in range(len(polynomial)):
            if k < len(factors):
                factors[k] += polynomial[k] * factor

    result = ""
    first = True
    for i in range(len(factors) - 1, -1, -1):
        factor = factors[i]
        if factor == 0:
            continue

        if factor.denominator == 1:
            factor_str = str(factor.numerator)
        else:
            factor_str = f"{factor.numerator}/{factor.denominator}"

        if not first:
            if factor > 0:
                result += " + "
            else:
                result += " - "
                factor_str = factor_str[1:]
        else:
            first = False

        if i == 0:
            result += factor_str
        elif i == 1:
            if factor == 1:
                result += "x"
            else:
                result += f"{factor_str}x"
        else:
            if factor == 1:
                result += f"x^{i}"
            else:
                result += f"{factor_str}x^{i}"
    return result

if __name__ == "__main__":
    print(main())