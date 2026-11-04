def is_unnatural_prime(n):
    str_num = str(n)
    remove_neg = str_num.replace('-','')
    number = int(remove_neg)

    devisors = range(2, number)

    if number < 2:
        return False

    for possible_devisor in devisors:
        if int(remove_neg)%possible_devisor == 0:
            return False
    return True


