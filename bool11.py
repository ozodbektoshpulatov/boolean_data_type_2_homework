def main(a):
    """ 
    Check a "number" is both positive and even
    Args:
        number: int
    Returns:
        bool
    """
    # Write your code here
    answer=(a>0 and a%2==0)
    return answer
print(main(4))