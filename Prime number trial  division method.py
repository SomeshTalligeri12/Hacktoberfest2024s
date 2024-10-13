def is_prime_trial_division(n):

    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):

        if n % i == 0:
            return False

    return True


# Test the function with n = 11
print(is_prime_trial_division(11))
