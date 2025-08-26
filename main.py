def main():
    n = int(input("Enter how many numbers the sequence should have: "))
    numbers = []
    for i in range(1, n+1):
        a = float(input(f"Enter a{i}:"))
        numbers.append(a)

    factors = [0.0] * n
    for i in range(n):
        denominator = 1
        for j in range(n):
            if j != i:
                denominator *= (i+1 - (j + 1))

        polynomial = [1.0]
        for j in range(n):
            if j != i:
                new = [0.0] * (len(polynomial) + 1)
                for k in range(len(polynomial)):
                    new[k] += polynomial[k] * (-(j+1))
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
        if not first:
            result += " + "
        else:
            first = False
        if i == 0:
            result += f"{factor}"
        elif i == 1:
            if factor == 1:
                result += "x"
            else:
                result += f"{factor}x"
        else:
            if factor == 1:
                result += f"x^{i}"
            else:
                result += f"{factor}x^{i}"
    return result

if __name__ == "__main__":
    print(main())