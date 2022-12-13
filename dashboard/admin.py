from django.contrib import admin

# Register your models here.

from .models import Barang
from .models import Transaksi
from .models import Detailtrans, Jenis, Member

class kolomBarang(admin.ModelAdmin):
    list_display=['kodebrg','nama', 'stok', 'link_gbr', 'jenis_id']
    search_fields=['kodebrg', 'nama']
    list_filter=['jenis_id']
    list_per_page=5


admin.site.register(Barang,kolomBarang)
admin.site.register(Transaksi)
admin.site.register(Detailtrans)
admin.site.register(Jenis)
admin.site.register(Member)