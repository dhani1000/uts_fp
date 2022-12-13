from django.shortcuts import render
from dashboard.forms import FormBarang
from dashboard.models import Barang, Jenis, Member

def produk(request):
    titelnya="Produk"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'produk.html',konteks)
# Create your views here.

def tambah_barang(request):
    form=FormBarang()
    titelnya="Daftar Barang"
    konteks={
        'form':form,
        'titel':titelnya,
    }
    return render(request,'tambah_barang.html', konteks)

def Barang_view(request):
    barangs=Barang.objects.all()
    titelnya="Daftar Barang"
    konteks={
        'barangs':barangs,
        'titel':titelnya,
    }
    return render(request,'tampil_brg.html', konteks)

def jenis(request):
    jeniss=Jenis.objects.all()
    titelnya="Jenis"
    konteks={
        'jeniss':jeniss,
        'titel':titelnya,
    }
    return render(request,'jenis.html', konteks)

def member(request):
    members=Member.objects.all()
    titelnya="Member"
    konteks={
        'members':members,
        'titel':titelnya,
    }
    return render(request,'member.html', konteks)