from django.db import models

# Tabel jenis buku
class Jenis(models.Model):
    jns_buku = models.CharField(max_length=50)
    jns_ket = models.TextField()

    def __str__(self) -> str:
        return self.jns_buku

# Tabel bahasa
class Bahasa(models.Model):
    bhs_buku = models.CharField(max_length=50)
    bhs_ket = models.TextField()

    def __str__(self) -> str:
        return self.bhs_buku

# Tabel Barang
class Barang(models.Model):
    brg_kode = models.CharField(max_length=8)
    brg_nama = models.CharField(max_length=100)
    brg_stok = models.IntegerField()
    brg_harga = models.BigIntegerField()
    brg_gambar = models.ImageField(upload_to='images/', blank=True)
    brg_waktuposting = models.DateTimeField(auto_now_add=True)
    brg_jenis = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)
    brg_bahasa = models.ForeignKey(Bahasa, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return "{}. {}".format(self.brg_kode, self.brg_nama)
