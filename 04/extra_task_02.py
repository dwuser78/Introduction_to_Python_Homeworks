import re

def optimize_view(raw_str: str) -> str:
    result: str = ""

    raw_str = raw_str.replace(' ', '')

    for i in range(len(raw_str)):
        if raw_str[i] == '*':
            if i + 1 < len(raw_str):
                if raw_str[i + 1].isdigit():
                    result += raw_str[i]
        elif raw_str[i] == '=':
            break
        else:
            result += raw_str[i]

    return result

def split_polynomial(pol: str):
    result = re.findall("[-+]?[\d*[A-Za-z]*]?\^?\d*", pol)

    return result

def split_monomial(monomial: str):
    digit = re.findall("^[-+]?\d*", monomial)
    if digit[0] == "-":
        digit[0] = "-1"
    elif digit[0] == "+":
        digit[0] = "1"

    vars = re.findall("(?:[A-Za-z])+(?:\^?\d+)*$", monomial)

    return int(digit[0]), str(vars[0]) if len(vars) > 0 else None

def add_similar(matches):
    res = []
    attempt = len(matches)
    first_dgt = True

    while attempt > 0:
        curr_dgt, curr_var = split_monomial(matches.pop(0))
        sum_dgt = curr_dgt
        for i, next_elem in enumerate(matches):
            if next_elem == "":
                del matches[i]
                continue

            next_dgt, next_var = split_monomial(next_elem)
            if next_var == curr_var:
                sum_dgt += next_dgt
                del matches[i]

        if curr_var == None:
            var = ""
        else:
            var = curr_var

        if sum_dgt > 1:
            if first_dgt:
                res.append(str(sum_dgt) + var)
            else:
                res.append("+" + str(sum_dgt) + var)
        elif sum_dgt < -1:
            res.append(str(sum_dgt) + var)
        else:
            if var == "":
                if first_dgt:
                    res.append(str(sum_dgt))
                else:
                    res.append("+" + str(sum_dgt))
            else:
                res.append(var)

        attempt = len(matches)
        first_dgt = False

    return res

polynomial_1 = input("Enter the first polynomial: ")
polynomial_2 = input("Enter the second polynomial: ")

# polynomial_1 = "2x^2 + 4x + 5 = 0"
# polynomial_2 = "5x^3 - x^2 - 12 = 0"

matches = split_polynomial(optimize_view(polynomial_1)) + \
          split_polynomial(optimize_view(polynomial_2))

print("Sum of polynomials: ", end="")
for monomial in add_similar(matches):
    print(monomial, end="")