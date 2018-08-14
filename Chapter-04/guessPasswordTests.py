import genetic
import datetime
import unittest


def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes) if expected == actual)

def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime 
    print("{}\t{}\t{}".format(''.join(candidate.Genes), candidate.Fitness, timeDiff))

class GuessPasswordTests(unittest.TestCase):
    
    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."

    def test_Hello_World(self): 
        target = "Hello World!" 
        self.guess_password(target)
    
    def test_For_I_am_fearfully_and_wonderfully_made(self): 
        target = "For I am fearfully and wonderfully made." 
        self.guess_password(target)

    def test_benchmark(self): 
        genetic.Benchmark.run(self.test_For_I_am_fearfully_and_wonderfully_made)
        
    def guess_password(self, target): 
        startTime = datetime.datetime.now()

        def fnGetFitness(candidate): 
            return get_fitness(candidate, target)

        def fnDisplay(candidate): 
            display(candidate, startTime)
        
        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target), optimalFitness, self.geneset, fnDisplay)
        self.assertEqual(''.join(best.Genes), target)

if __name__ == '__main__':   
    unittest.main()