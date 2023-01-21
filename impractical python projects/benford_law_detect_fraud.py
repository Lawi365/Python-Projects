#  BENFORD FRAUD DETECTION
#  2023-20-January
#  project no 3. 2023
# code rewritten in python by : Lawi365

import sys
import math
from collections import defaultdict
import matplotlib.pyplot as plt

"""
Using Benfords law to detect Fraud in US Election.
"""
# Bens percentages for leading digits 1-9
BENFORD = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]


def load_data(filename):
    """Opens existing text file & returns a list of strings.

    Args:
        filename (_type_): File name for this case i'll place them in 
        the same folder as this py file. for simpler reasons.
    """

    with open(filename) as f:
        # read the file taking care of the newline \n
        return f.read().strip().split('\n')


def count_first_digits(data_list):
    """
    Count 1st digits in list of numbers

    Args:
        data_list (_type_): _description_
        
    Returns: counts and frequency.
    
    """

    first_digits = defaultdict(int)

    for sample in data_list:
        if sample == '':
            continue
        try:
            int(sample)
        except ValueError as e:
            print(e, file=sys.stderr)
            print("Sample must be integers. Exiting", file=sys.stderr)
            sys.exit(1)

        first_digits[sample[0]] += 1

    # check for missing digits.
    keys = [str(digit) for digit in range(1, 10)]
    for key in keys:
        if key not in first_digits:
            first_digits[key] = 0

    data_count = [v for (k, v) in sorted(first_digits.items())]
    total_count = sum(data_count)

    data_pct = [(i / total_count) * 100 for i in data_count]
    return data_count, data_pct, total_count


def get_expected_counts(total_count):
    """Returns a list of expected Bens' law counts for a total sample count.

    Args:
        total_count (_type_): _description_
    """

    return [round(p * total_count / 100) for p in BENFORD]


def chi_square_test(data_count, expected_counts):
    """Return boolean on chi-square test ( 8df pval = .05)"""
    chi_square_stat = 0
    for data, expected in zip(data_count, expected_counts):
        chi_square = math.pow(data - expected, 2)
        chi_square_stat += chi_square / expected

    print(f'\n Chi Squared Test Stat = {chi_square_stat}')
    print('Critical value at a pval of 0.05 is 15.51')

    return chi_square_stat < 15.51


def bar_chart(data_pct):
    """Make bar chart of observed vs expxected 1st digit freq %"""

    fig, ax = plt.subplots()

    index = [i + 1 for i in range(len(data_pct))]

    fig.canvas.setWindowTitle('Percentage First Digits')
    ax.set_title('Data vs Bens Values', fontsize=15)
    ax.set_ylabel('Frequency (%)', fontsize=16)
    ax.set_xticks(index)
    ax.set_xticklabels(index, fontsize=14)
    
    #BUILD THE BARS.
    rects = ax.bar(index, data_pct, width=.95,color='black',label='Data')
    
    #attach a text label above each bar displaying its height.
    
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, height, '{:0.1f}'.format(height), ha='center', va='bottom',fontsize=13)
        
        
    #plot Bens values as red dots.
    ax.scatter(index, BENFORD, s=150, c='red',zorder=2,label='Benford')
    
    
    #hide the right and top spines & add legend.
    
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.legend(prop={'size': 15}, frameon=False)
    
    plt.show()


# DEFINE MAIN. WHITE

def main():
    """Call functions and print req stats"""
    
    #load the data
    while 1 :
        filename = input('Name of file with Count Data: ')
        try:
            data_list = load_data(filename)
            
        except IOError as e:
            print(f"{e}. Try again")
            
        else:
            break
        
    data_count, data_pct, total_count= count_first_digits(data_list)
    expected_counts = get_expected_counts(total_count)
    print('Observed counts = {}'.format(data_count))
    
    print('Expected counts = {}'.format(expected_counts), '\n')
    
    
    print("First Digit Probabilites")
    for i in range(1, 10):
        print("{}. observed: {:.3f} expected: {:.3f}".format(
            i, data_pct[i -1] / 100, BENFORD[i-1]/ 100
        ))
    if chi_square_test(data_count, expected_counts):
        print("Observed distribution mathces expected distribution")
    else:
        print('Observed distribution does not match expected.', file=sys.stderr)
        
    bar_chart(data_pct)
    
#CALL OUT THE MAIN
if __name__ == '__main__':
    main()
        