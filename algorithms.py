from functools import lru_cache
from typing import Generator
from enum import IntEnum

class AlgSimple():
    '''простые алгоритмы'''

    @lru_cache(maxsize=None)
    def fib_rec(self, n):
        '''Фибоначчи на рекурсии (с мемоизацией)'''
        if n < 2:
            return n
        return self.fib_rec(n-1) + self.fib_rec(n-2)

    def fib_max(self, n: int) -> Generator[int, None, None]:
        '''Самый быстрый Фибоначчи на циклах и генераторах'''
        yield 0
        if n < 2:
            yield 1
        # начальные значения
        last = 0
        next = 1
        for _ in range(1, n):
            old_next = next
            next = last + next
            last = old_next
            yield next

class dnk():
    ''' Нуклеотид(ACGT) - кодон(последов-ть 3 нуклеодитов) - ген'''
    def __init__(self):
        self.Nucleotide = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

    def get_gene(self, str_nucl:str) -> list:
        '''Из строки генов -->> последовательность кодонов'''
        self.gene = []
        for i in range(0, len(str_nucl), 3):
            if (i + 2) <= len(str_nucl):
                codon = (
                    self.Nucleotide[str_nucl[i]], 
                    self.Nucleotide[str_nucl[i+1]], 
                    self.Nucleotide[str_nucl[i+2]]
                )
                self.gene.append(codon)
        return self.gene

    def get_exists_codon(self, codon):
        '''
        Проверить наличие кодона в гене (бинарный поиск)
        в работе можно воспользоваться библиотекой bisect(!)
        NOTE: с постоянной сортировкой вся выгода от бин.поиска теряется (!)
        '''
        low = 0
        high = len(self.gene) - 1
        gene_sort = sorted(self.gene)

        while low <= high:
            mean = int(high / 2)
            if gene_sort[mean] == codon:
                return True
            elif gene_sort[mean] > codon:
                high = mean - 1
            else:
                low = mean + 1
        return False


if __name__ == '__main__':
    str_test = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"
    # alg = AlgSimple()
    d = dnk()
    # для проверки бинарного поиска
    test_codon = (d.Nucleotide.A, d.Nucleotide.C, d.Nucleotide.G)
    d.get_gene(str_test)
    a = 1