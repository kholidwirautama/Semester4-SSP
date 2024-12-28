from django.shortcuts import render, redirect
from depot.forms import *
from depot.models import *
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.\
def login(request):
    pagetitle = "Home"
    konteks = {
        'title': pagetitle,
    }
    return render(request, "login.html", konteks)

def register(request):
    pagetitle = "Home"
    konteks = {
        'title': pagetitle,
    }
    return render(request, "register.html", konteks)

def home_redirect(request):
    return redirect('home')

def home(request):
    pagetitle = "Home"
    konteks = {
        'title': pagetitle,
    }
    return render(request, "home.html", konteks)

def produk(request):
    pagetitle = 'Produk'
    barangs = Barang.objects.all()
    konteks = {
        'title': pagetitle,
        'barangs': barangs,
    }
    return render(request, "produk.html", konteks)

def guildmember(request):
    pagetitle='Karakter'
    konteks = {
        'title':pagetitle
    }
    return render(request,"guildmember.html",konteks)

def kontak(request):
    pagetitle="Kontak"
    konteks = {
        'title':pagetitle,
    }
    return render(request,"kontak.html",konteks)

def tambah_barang(request):
    pagetitle="Tambah Barang"
    if request.method == 'POST':
        form = FormBarang(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Barang berhasil ditambahkan!')
            return redirect('tambah_barang')
    else:
        form = FormBarang()

    context = {
        'title':pagetitle,
        'form': form
    }
    return render(request, 'tambah_barang.html', context)

def tambah_bahasa(request):
    pagetitle="Tambah Bahasa"
    if request.method == 'POST':
        form = FormBahasa(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bahasa berhasil ditambahkan!')
            return redirect('tambah_bahasa')
    else:
        form = FormBahasa()

    context = {
        'title':pagetitle,
        'form': form
    }
    return render(request, 'tambah_bahasa.html', context)

def tambah_jenis(request):
    pagetitle="Tambah Jenis"
    if request.method == 'POST':
        form = FormJenis(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Jenis berhasil ditambahkan!')
            return redirect('tambah_jenis')
    else:
        form = FormJenis()

    context = {
        'title':pagetitle,
        'form': form
    }
    return render(request, 'tambah_jenis.html', context)

def tampil_barang(request):
    pagetitle = 'Edit'
    barangs_list = Barang.objects.all()
    paginator = Paginator(barangs_list, 10)
    page = request.GET.get('page')
    try:
        barangs = paginator.page(page)
    except PageNotAnInteger:
        barangs = paginator.page(1)
    except EmptyPage:
        barangs = paginator.page(paginator.num_pages)

    jeniss = Jenis.objects.all()
    bahasas = Bahasa.objects.all()
    context = {
        'title': pagetitle,
        'barangs': barangs,
        'jeniss': jeniss,
        'bahasas': bahasas,
    }
    return render(request, 'tampil_barang.html', context)

def ubah_barang(request, id_barang):
    pagetitle = 'Ubah Barang'
    barangs = Barang.objects.get(id=id_barang)
    if request.POST:
        form = FormBarang(request.POST, request.FILES, instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diubah")
            return redirect('tampil_barang')
    else:
        form = FormBarang(instance=barangs)

    konteks = {
        'title': pagetitle,
        'form': form,
        'barangs': barangs
    }
    return render(request, "ubah_barang.html", konteks)

def ubah_bahasa(request, id_bahasa):
    pagetitle = 'Ubah Bahasa'
    bahasa = Bahasa.objects.get(id=id_bahasa)
    if request.POST:
        form = FormBahasa(request.POST, instance=bahasa)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Bahasa Berhasil Diubah")
            return redirect('tampil_barang')
    else:
        form = FormBahasa(instance=bahasa)

    konteks = {
        'title': pagetitle,
        'form': form,
        'bahasa': bahasa
    }
    return render(request, "ubah_bahasa.html", konteks)

def ubah_jenis(request, id_jenis):
    pagetitle = 'Ubah Jenis'
    jenis = Jenis.objects.get(id=id_jenis)
    if request.POST:
        form = FormJenis(request.POST, instance=jenis)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Jenis Berhasil Diubah")
            return redirect('tampil_barang')
    else:
        form = FormJenis(instance=jenis)

    konteks = {
        'title': pagetitle,
        'form': form,
        'jenis': jenis
    }
    return render(request, "ubah_jenis.html", konteks)

def hapus_barang(request, id_barang):
    barang = Barang.objects.get(id=id_barang)
    barang.delete()
    messages.success(request, "Barang berhasil dihapus")
    return redirect('tampil_barang')

def hapus_bahasa(request, id_bahasa):
    bahasa = Bahasa.objects.get(id=id_bahasa)
    bahasa.delete()
    messages.success(request, "Bahasa berhasil dihapus")
    return redirect('tampil_barang')

def hapus_jenis(request, id_jenis):
    jenis = Jenis.objects.get(id=id_jenis)
    jenis.delete()
    messages.success(request, "Jenis berhasil dihapus")
    return redirect('tampil_barang')
