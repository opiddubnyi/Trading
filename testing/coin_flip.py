from random import randint


def prob(p):
    """ 0<= p <= 1, desired probability function"""
    p = p * 100
    r = randint(0, 100)
    if p >= r:
        return True
    else:
        return False



def check_prob(pr):
    res = []
    dic = {}
    for i in range(0, 1000):
        res.append(prob(pr))

    for i in range(len(res)):
        dic[res[i]] = res.count(res[i])
# comment kk
    return dic


def game(account_size, profit_factor, risk_per_trade, iterations=1000, p=0.5):
    """bet_size - % from account size
        1% <= bet <= 51%"""
    original = account_size
    for i in range(iterations):
        bet = risk_per_trade / 100 * account_size
        if account_size >= original * 0.01:
            if prob(p):
                account_size += bet * profit_factor
            else:
                account_size -= bet
        else:
            return ('failed on {} iteration'.format(i))

    return account_size


for i in range(1, 51):
    print('start_account_size - 10000, end - {}, risk per trade - {}%'.
          format(game(20000, 2.07, i, 190, 0.492), i))