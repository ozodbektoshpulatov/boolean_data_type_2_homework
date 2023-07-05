def main(a):
    """
    Check if a given number is negative or odd.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a<0 or a%2==1
print(main(-5))