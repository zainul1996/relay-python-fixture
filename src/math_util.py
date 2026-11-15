def add(left: int, right: int) -> int:
    return left + right


def gcd(left: int, right: int) -> int:
    left, right = abs(left), abs(right)
    while right:
        left, right = right, left % right
    return left
