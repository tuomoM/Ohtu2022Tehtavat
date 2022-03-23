





class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
     
        self.ljono = [] 


    def kuuluu(self, n):
        for x in self.ljono:
            if n == x:
                return True
        return False

    def lisaa(self, n):
        if self.kuuluu(n):
            return False       
        self.ljono.append(n)
        return True
    

    def poista(self, n):
        for x in self.ljono:
            if x == n:
                self.ljono.remove(x)
                return True
        return False
   

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return len(self.ljono)

    def to_int_list(self):
        taulu = []
        for i in self.ljono:
            taulu.append(i)
        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in a_taulu:
            x.lisaa(i)

        for i in b_taulu:
            x.lisaa(i)

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in a_taulu:
            for j in b_taulu:
                if i == j:
                    y.lisaa(i)

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
   
        tuloste = "{"
        eka = True
        for n in self.ljono:
            if(not eka):
              tuloste = tuloste +", "+ str(n) 
            else:
               tuloste = tuloste + str(n)
               eka = False    
        tuloste = tuloste + "}"
        return tuloste
