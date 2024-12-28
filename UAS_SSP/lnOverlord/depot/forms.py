from django.forms import ModelForm
from depot.models import *
from django import forms

class FormJenis(ModelForm):
    class Meta:
        model = Jenis
        fields = '__all__'

        widgets = {
            'jns_buku': forms.TextInput(attrs={'class': 'form-control'}),
            'jns_ket': forms.Textarea(attrs={'class': 'form-control'}),
        }

class FormBahasa(ModelForm):
    class Meta:
        model = Bahasa
        fields = '__all__'

        widgets = {
            'bhs_buku': forms.TextInput(attrs={'class': 'form-control'}),
            'bhs_ket': forms.Textarea(attrs={'class': 'form-control'}),
        }

class FormBarang(ModelForm):
    class Meta:
        model = Barang
        fields = '__all__'

        widgets = {
            'brg_kode': forms.TextInput(attrs={'class': 'form-control'}),
            'brg_nama': forms.TextInput(attrs={'class': 'form-control'}),
            'brg_stok': forms.NumberInput(attrs={'class': 'form-control'}),
            'brg_harga': forms.NumberInput(attrs={'class': 'form-control'}),
            'brg_gambar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'brg_jenis': forms.Select(attrs={'class': 'form-control'}),
            'brg_bahasa': forms.Select(attrs={'class': 'form-control'}),
        }
