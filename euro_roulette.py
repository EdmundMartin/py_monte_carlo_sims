from random import randint
import matplotlib
import matplotlib.pyplot as plt

punter_balance = 100
punter_fixed_wager = 1

def single_number_guess():
    return randint(0,36)

def single_number_bet(wager,guess):
    wheel_spin = randint(0,36)
    if guess == wheel_spin:
        return (wager * 35) + wager
    else:
        return 0

def run_simulation_single_number(balance,fixed_wager):
    balances_to_plot = []
    wagers_to_plot = []
    wager = 0
    balances_to_plot.append(balance)
    wagers_to_plot.append(wager)
    while balance > 0:
        balance -= fixed_wager
        change_in_balance = single_number_bet(fixed_wager,single_number_guess())
        balance += change_in_balance
        print(balance)
        wager += 1
        wagers_to_plot.append(wager)
        balances_to_plot.append(balance)
    plt.plot(wagers_to_plot,balances_to_plot)

run_simulation_single_number(punter_balance,punter_fixed_wager)

plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()
