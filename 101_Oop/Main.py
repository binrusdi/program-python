class Manusia:
  def __init__(self, tinggi, bb, wkulit):
    self.tinggi = tinggi
    self.bb = bb
    self.wkulit = wkulit
    
  def makan(self): # ini method object
    if self.bb >= 70 or self.tinggi >= 170:
      print("Makan nya banyak, kaya gorila")
    elif self.bb <= 50 or self.tinggi <= 150:
      print("Makannya kurang, takut cacingan")
  
  def suku(self): # ini method object
    if self.wkulit == "putih":
      print("Dia Orang barat")
    elif self.wkulit == "sawo matang":
      print("Orang Asia")
    else:
      print("Orang Afrika")
      
orangKeSatu = Manusia(70, 50, "sawo matang")
orangKeSatu.suku() # method object tidak perlu menggunakan print()
orangKeSatu.makan() # method object tidak perlu menggunakan print()
print(orangKeSatu.wkulit) # ini adalah atribut/prop object