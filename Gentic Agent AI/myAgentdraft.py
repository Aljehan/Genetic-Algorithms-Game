import numpy as np

playerName = "myAgent"
nPercepts = 75  #This is the number of percepts
nActions = 7    #This is the number of actionss


class MyCreature:

    def __init__(self):

       self.chromosome = np.random.rand.normal(size = (75,7))

    def AgentFunction(self, percepts):
        actions = np.matmul(percepts.flatten(),self.chromosome)
        return actions



def get_function (pupolation):
    fitness = np.zeros(30)
    for n.creature in enumrate(pupolation):
        fitness[n] = creature.turn + creature.alive + creature.size + creature.strawb_eats + creature.enemy_eats



def mutate (creature):
    for i in range[75]:
        for j in range[7]:
            if(np.random.rand()<0.2):
                creature.chromosome[i][j] += np.random.normal()
                #-------------Clipping---------------
                if(creature.chromosome[i][j] > 1):
                    creature.chromosome[i][j]=1
                elif(creature.chromosome[i][j]< -1):
                    creature.chromosome[i][j] = -1

    return creature
#------------------------------------------------------------------------------



def crossover(creature1, creature2):
    crossed_chromosome = np.zeros((75,7))
    for i in range(75):
        for j in range(7):
            if (np.random.rand()<0.5):
                crossed_chromosome[i][j] = creature1[i][j]
            else:
                crossed_chromosome = creature2[i][j]
    return crossed_chromosome

def newGeneration(old_population):

    fitness = get_function(old_population)
    for n, creature in enumerate(old_population):

        fitness[n] = creature.turn
    new_population = list()

    #=============EVOLVING===============
    for n in range(30):
        parents = np.random.choice(old_population,size=2,replace = False,p=fitness)
        baby = MyCreature()
        baby.chromosome = crossover(parents[0],parents[1])
        if(np.random.rand()<MUTATIONRATE):
            baby = mutate(baby)

        new_population.append(baby)

    avg_fitness = np.mean(fitness)

    return (new_population, avg_fitness)
