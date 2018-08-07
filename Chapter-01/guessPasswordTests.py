import genetic
import datetime
import unittest


def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes) if expected == actual)

def display(guess, target, startTime):
    timeDiff = datetime.datetime.now() - startTime 
    fitness = get_fitness(guess, target) 
    print("{}\t{}\t{}".format(guess, fitness, timeDiff))

class GuessPasswordTests(unittest.TestCase):
    
    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."

    def test_Hello_World(self): 
        target = "Hello World!" 
        self.guess_password(target)

    def guess_password(self, target): 
        startTime = datetime.datetime.now()

        def fnGetFitness(genes): 
            return get_fitness(genes, target)

        def fnDisplay(genes): 
            display(genes, target, startTime)
        
        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target), optimalFitness, self.geneset, fnDisplay)
        self.assertEqual(best, target)

if __name__ == '__main__':   
    unittest.main()