from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect, render
from django.conf import settings
from django.conf.urls.static import static
from depot.views import *

urlpatterns = [
    path('', home_redirect),
    path('admin/', admin.site.urls),
    path('login/', login),
    path('register/', register),
    path('home/', home, name='home'),
    path('produk/', produk),
    path('guildmember/', guildmember),
    path('kontak/', kontak),
    path('tambahbarang/', tambah_barang, name='tambah_barang'),
    path('tambahbahasa/', tambah_bahasa, name='tambah_bahasa'),
    path('tambahjenis/', tambah_jenis, name='tambah_jenis'),
    path('tampilbarang/', tampil_barang, name='tampil_barang'),
    path('ubahbarang/<int:id_barang>/', ubah_barang, name='ubah_barang'),
    path('ubahbahasa/<int:id_bahasa>/', ubah_bahasa, name='ubah_bahasa'),
    path('ubahjenis/<int:id_jenis>/', ubah_jenis, name='ubah_jenis'),
    path('hapusbarang/<int:id_barang>/', hapus_barang, name='hapus_barang'),
    path('hapusbahasa/<int:id_bahasa>/', hapus_bahasa, name='hapus_bahasa'),
    path('hapusjenis/<int:id_jenis>/', hapus_jenis, name='hapus_jenis'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
