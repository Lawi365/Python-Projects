import time
import random 
import statistics
import matplotlib.pyplot as plt

#Today  WE ARE BREEDING RATS TO MATCH OUR TARGET GOAL OF 50,000 GRAMS.
# USING GENETIC ALGORITHM ....
# WRITTEN 20TH JAN 2023
# BY LAWI365.
# ADDED VISUALIZATION INTO IT HAVE FUN AND WATCH THE RATS GROW

#  CONSTANTS (weights are in grams)
GOAL = 50000
NUM_RATS = 50
INIT_MIN_WT = 200
INIT_MAX_WT = 600
INIT_MODE_WT = 300
MUTATE_ODDS = 0.05
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
LITTER_SIZE = 8
LITTERS_PER_YEAR = 10
GENERATION_LIMIT = 100

# we need to ensure even-number of rats for breeding pairs:
if NUM_RATS % 2 != 0:
    NUM_RATS += 1
    

def populate(num_rats, min_wt, max_wt, mode_wt):
    """Initialise a population with a triangular distribution of weights.

    Args:
        num_rats (_type_): _description_
        min_wt (_type_): _description_
        max_wt (_type_): _description_
        mode_wt (_type_): _description_
    """
    
    return [int(random.triangular(min_wt, max_wt,mode_wt)) for i in range(num_rats)]

def fitness(population, goal):
    """Measure population fitness based on an attribute mean vs target.

    Args:
        population (_type_): _description_
        goal (_type_): _description_
    """
    ave = statistics.mean(population)
    
    return ave/goal

def select(population, to_retain):
    """cull a population to retain only a specified number of members."""
    
    sorted_population = sorted(population)
    to_retain_by_sex = to_retain//2
    members_per_sex = len(sorted_population) // 2
    
    females = sorted_population[:members_per_sex]
    males = sorted_population[members_per_sex:]
    
    selected_females = females[-to_retain_by_sex:]
    selected_males = males[-to_retain_by_sex:]
    
    return selected_males, selected_females

def breed(males,females, litter_size):
    """Crossover genes among members (weights) of a population.

    Args:
        males (_type_): _description_
        females (_type_): _description_
        litter_size (_type_): _description_
    """
    random.shuffle(males)
    random.shuffle(females)
    
    children = []
    
    for male, female in zip(males, females):
        for child in range(litter_size):
             child = random.randint(female, male)
             children.append(child)
             
    return children

def mutate(children,mutate_odds, mutate_min, mutate_max):
    """Randomly alter rat weights using input odds & fractional changes.

    Args:
        children (_type_): _description_
        mutate_odds (_type_): _description_
        mutate_min (_type_): _description_
        mutate_max (_type_): _description_

    Returns:
        _type_: _description_
    """
    for index, rat in enumerate(children):
        if mutate_odds >= random.random():
            children[index] = round(rat*random.uniform(mutate_min, mutate_max))

    return children

def main():
    """Init population, select, breed and mutate, display  results.
    """
    generations = 0
    parents = populate(NUM_RATS,INIT_MIN_WT,INIT_MAX_WT,INIT_MODE_WT)
    print("initial pop weights = {}".format(parents))
    
    popul_fitness = fitness(parents,GOAL) 
    print("Initial pop fitness = {}".format(popul_fitness))
    print("Number to retain = ",NUM_RATS)
    
    ave_wt = []
    
    while popul_fitness < 1 and generations < GENERATION_LIMIT:
        selected_males, selected_females = select(parents,NUM_RATS)
        child = breed(selected_males,selected_females,LITTER_SIZE)
        children = mutate(child,MUTATE_ODDS,MUTATE_MIN,MUTATE_MAX)
        parents = selected_males + selected_females + children
        
        popul_fitness = fitness(parents,GOAL)
        print(' Generation {} fitness = {:.4f}'.format(generations,popul_fitness))
        ave_wt.append(int(statistics.mean(parents)))
        generations += 1
        
        plt.plot(ave_wt)
        plt.xlabel('generation')
        plt.ylabel('Average Weight')
       
        # print("average weight per generaton = {}".format(ave_wt))
        # print("\n number of generations = {}".format(generations))
        print(" number of years = {}".format(int(generations/LITTERS_PER_YEAR)))
    plt.show()
if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print("\n Runtime for this program was {} seconds".format(duration))