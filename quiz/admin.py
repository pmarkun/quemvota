from django.contrib import admin

# Register your models here.
from quiz.models import Proposicao, Parlamentar, CasaLegislativa, Votacao

class ProposicaoAdmin(admin.ModelAdmin):
    list_display = ('id_prop', 'ementa')
    search_fields = ('id_prop','ementa', 'hashtags')

class ParlamentarAdmin(admin.ModelAdmin):
    list_display = ('nome','partido', 'situacao')
    search_fields = ('nome',)
    list_filter = ('partido', 'situacao')
    ordering = ('-situacao','nome')


admin.site.register(Proposicao, ProposicaoAdmin)
admin.site.register(Parlamentar, ParlamentarAdmin)
admin.site.register(CasaLegislativa)
admin.site.register(Votacao)
