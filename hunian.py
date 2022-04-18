class Hunian():
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, listrik = 0):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.listrik = listrik

    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_dokumen(self):
        pass
    
    def get_listrik(self):
        return self.listrik

    def get_summary(self):
        return "Hunian "+ self.jenis +" \nDitempati oleh " + str(self.jml_penghuni) + " orang" + "\nJumlah kamar : " + str(self.jml_kamar) + "\nListrik : " + str(self.listrik) + " Watt"