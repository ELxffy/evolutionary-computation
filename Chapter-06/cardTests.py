import unittest
import datetime
import genetic
import operator
import functools
import random


class Fitness:

    def __init__(self, group1Sum, group2Product, duplicateCount):
        self.Group1Sum = group1Sum
        self.Group2Product = group2Product
        sumDifference = abs(36 - group1Sum)
        productDifference = abs(360 - group2Product) 
        self.TotalDifference = sumDifference + productDifference 
        self.DuplicateCount = duplicateCount

    def __gt__(self, other):
        if self.DuplicateCount != other.DuplicateCount:
            return self.DuplicateCount < other.DuplicateCount
        return self.TotalDifference < other.TotalDifference
    
    def __str__(self):
        return "sum: {} prod: {} dups: {}".format(self.Group1Sum,
                                                    self.Group2Product,
                                                    self.DuplicateCount)


def get_fitness(genes):

    group1Sum = sum(genes[0:5])
    group2Product = functools.reduce(operator.mul, genes[5:10]) 
    duplicateCount = (len(genes) - len(set(genes)))
    return Fitness(group1Sum, group2Product, duplicateCount)


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime 
    print("{} --- {}\t{}\t{}".format(', '.join(map(str, candidate.Genes[0:5])), 
                                    ', '.join(map(str, candidate.Genes[5:10])),
                                    candidate.Fitness, 
                                    timeDiff))


def mutate(genes, geneset):
    if len(genes) == len(set(genes)):
        mutCount = random.randint(1,4)
        while mutCount > 0:
            mutCount -=1
            indexA, indexB = random.sample(range(len(genes)), 2) 
            genes[indexA], genes[indexB] = genes[indexB], genes[indexA]
    else:
        indexA = random.randrange(0, len(genes)) 
        indexB, indexBa = random.randrange(0, len(geneset), 2) 
        genes[indexA] = geneset[indexBa]\
                        if geneset[indexB] == genes[indexA] \
                        else geneset[indexB]


class CardTests(unittest.TestCase): 
    
    def test(self):

        geneset = [i + 1 for i in range(10)]
        startTime = datetime.datetime.now()

        def fnDisplay(candidate): 
            display(candidate, startTime)

        def fnGetFitness(genes): 
            return get_fitness(genes)
        
        def fnMutate(genes): 
            return mutate(genes, geneset)
        
        optimalFitness = Fitness(36, 360, 0)       
        best = genetic.get_best(fnGetFitness, 10, optimalFitness,
                                geneset, fnDisplay, custom_mutate=fnMutate)
        
        self.assertTrue(not optimalFitness > best.Fitness)

    def test_benchmark(self): 
        genetic.Benchmark.run(lambda: self.test())

if __name__ == '__main__':   
    unittest.main()

    
