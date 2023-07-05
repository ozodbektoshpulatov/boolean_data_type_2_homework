def main(a):
    """
    Check if a given number is divisible by either 3 or 5.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    answer=(a>0 ,a%2==0)
    return answer
print(main(8))
