from typing import Union


# Task 1
def to_power(x: Union[int, float], exp: int) -> Union[int, float, None]:
    if exp <= 0:
        raise ValueError("This function works only with exp > 0")
    if exp == 1:
        return x
    return x * to_power(x, exp-1)


# Task 2
def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) <= 2:
        return True
    if looking_str[0] == looking_str[-1] and is_palindrome(looking_str[1:-1]):
        return True
    else:
        return False


# Task 3
def mult(a: int, n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return a
    return a + mult(a, n-1)


# Task 4
def reverse(input_str: str) -> str:
    if input_str == '':
        return ''
    return input_str[-1] + reverse(input_str[:-1])


# Task 5
def sum_of_digits(digit_string: str) -> int:
    if len(digit_string) == 1:
        return int(digit_string)
    return int(digit_string[-1]) + sum_of_digits(digit_string[:-1])


def main():
    print(to_power(2, 3))
    print(is_palindrome("asdfggfdsa"))
    print(mult(3, 4))
    print(reverse('qwer'))
    print(sum_of_digits('234'))


if __name__ == '__main__':
    main()
