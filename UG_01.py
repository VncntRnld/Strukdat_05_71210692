
class Mobil:

    _merk = None
    _tipe = None
    _kapasitasBBM = None
    _jenisBahanBakar = None

    def __init__(self, merk, tipe):
        self._merk = merk
        self._tipe = tipe

    def setJenisBahanBakar(self, jenisBBM):
        self._jenisBahanBakar = jenisBBM

    def setKapasitasBBM(self, kapasitas):
        self._kapasitasBBM = kapasitas

    def getMerk(self):
        return self._merk
    
    def getTipe(self):
        return self._tipe

    def getJenisBahanBakar(self):
        return self._jenisBahanBakar

    def getKapasitasBBM(self): 
        return self._kapasitasBBM

    def printInfo(self):
        print("========== INFO ============")
        print("Merk            : {}" .format(self.getMerk()))
        print("Tipe            : {}" .format(self.getTipe()))
        print("Bahan Bakar     : {}" .format(self.getJenisBahanBakar()))
        print("Kapasitas BBM   : {}" .format(self.getKapasitasBBM()))

    def isiBBM(self, harga):
        if self._jenisBahanBakar == None or self._kapasitasBBM == None:
            print("ERROR! Kapasitas BBM atau Jenis Bahan Bakar belum di inputkan")
        else:
            print("Mengisi {} Liter" .format(self.getKapasitasBBM()))
            print("Total Harga : Rp{}" .format(harga * self.getKapasitasBBM()))

if __name__ == "__main__":
    mobil1 = Mobil("Toyota", "Avanza")
    mobil1.printInfo()

    mobil2 = Mobil("Nissan", "Grand Livina")
    mobil2.setJenisBahanBakar("Bensin")
    mobil2.setKapasitasBBM(20)
    mobil2.printInfo()

    mobil1.isiBBM(14500)
    mobil2.isiBBM(14500)        
