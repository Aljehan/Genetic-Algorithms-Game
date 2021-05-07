import numpy as np

class MyCreature:
    def __init__(self):
        #creat a chromosome containing 525 elemnts in a 2D list
        self.chromosomes = np.random.normal(size=(75,7))
        #use matrix multiplacation to map the action
    def AgentFunction(self, percepts):
        #(1,75)matmul(75,7) = (1,7)
        actions = np.matmul(percepts.flatten(),self.chromosomes)
        return actions

#-Mix the genes of the parents to create a new creature
def crossover(creature1,creature2):
    # Create a 2D list of zeros
    crossed_chromosome = np.zeros((75,7))
    #UNIFORM CROSSOVER
    #[1][2][3][4][5][6] CREATURE1 example
    #[2][4][1][5][6][3] CREATURE2 example
    #[2][4][3][4][6][6] RESULT example
    for i in range(75):
        for j in range(7):
            if(np.random.rand()<0.5):
                #----50% chance we choose creature1's gene----
                crossed_chromosome[i][j] = creature1.chromosomes[i][j]
            else:
                #---50% chance we choose creature2's gene-----
                crossed_chromosome[i][j] = creature2.chromosomes[i][j]
            #Mutation of crossed chromosome
            if(np.random.rand()<0.1):
                #  -1<np.random.normal() <1(most of the times)
                crossed_chromosome[i][j] += np.random.normal()*0.1
    return crossed_chromosome

# Measure the fitness score of every creature in the population.
def get_fitness(population):
    fitness = np.zeros(len(population))
    for n,creature in enumerate(population):
        fitness[n] = creature.turn/10 + 10*creature.alive + 5*creature.size + 15*creature.strawb_eats + 20*creature.enemy_eats
    return fitness

# Help converting the fitness into values between 0-1
def normalize_fitness(fitness):
    fitness_sum = sum(fitness) 
    fitness = fitness/fitness_sum
    return fitness

def newGeneration(old_population):
    #-------Get Fitness----------
    fitness = get_fitness(old_population)    
    #-------EVOLVING-------------
    new_population = list()
    for n in range(34):
        #parents should return a list of two elements, which are both creatures(roullete wheel).
        parents = np.random.choice(old_population,size=2,replace=False,p=normalize_fitness(fitness))
        baby = MyCreature()
        baby.chromosomes = crossover(parents[0],parents[1])
        #add the new creature to the new population.
        new_population.append(baby)

    avg_fitness = np.mean(fitness)
    return (new_population, avg_fitness)
