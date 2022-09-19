"""
Codingbat Warmup-1 sleep_in
"""
def sleep_in(weekday, vacation):
    """
    The parameter weekday is True if it is a weekday, and the parameter
    vacation is True if we are on vacation. We sleep in if it is not a
    weekday or we're on vacation. Return True if we sleep in.
    """
    return not weekday or vacation

def main():
    """
    Main function
    """
    print(sleep_in(False, False))
    print(sleep_in(True, False))
    print(sleep_in(False, True))

if __name__ == "__main__":
    main()