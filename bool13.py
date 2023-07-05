def main(a):
    """
    Check if the given number is divisible by only one of 3 or 5.
    Args:
        b: int
    Returns:
        bool
    """
    # Write your code here
    answer=(a%3==0 or a%5==0) and (a%15!=0)
    return answer