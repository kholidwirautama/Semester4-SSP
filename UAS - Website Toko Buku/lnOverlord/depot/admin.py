from django.contrib import admin
from .models import Barang, Jenis, Bahasa

class kolomBarang(admin.ModelAdmin):
    list_display = ['brg_kode', 'brg_nama', 'brg_stok', 'brg_harga', 'brg_gambar', 'brg_jenis', 'brg_bahasa']
    search_fields = ['brg_kode', 'brg_nama']
    list_filter = ('brg_jenis',)
    list_per_page = 10

class kolomBahasa(admin.ModelAdmin):
    list_display = ['bhs_buku', 'bhs_ket']
    search_fields = ['bhs_buku']
    list_per_page = 10

class kolomJenis(admin.ModelAdmin):
    list_display = ['jns_buku', 'jns_ket']
    search_fields = ['jns_buku']
    list_per_page = 10

admin.site.register(Barang, kolomBarang)
admin.site.register(Jenis, kolomJenis)
admin.site.register(Bahasa, kolomBahasa)