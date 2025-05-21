class Computer :
    def __init__(self, math, physique, chimie):
        self.mon_cpu = math
        self.ma_ram = physique
        self.mon_disk = chimie


    def configuration(self):
        print(self.mon_cpu,self.ma_ram,self.mon_disk)


    def compare(self,autre):
        return self.mon_cpu == autre.mon_cpu


    def modify_cpu(self, new_cpu):
        self.mon_cpu = new_cpu

    def moyenne(self):
        return (self.mon_cpu + self.ma_ram + self.mon_disk)/3



alpha = Computer(8,16,10)
alseny = Computer(2, 8, 9)

print(alpha.moyenne())
print(alseny.moyenne())

if alpha.compare(alseny):
    print("les deux ordi ont les même cpu")
else :
    print("il n'ont pas les même cpu")
