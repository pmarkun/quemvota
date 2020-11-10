from django.contrib import admin

# Register your models here.
from quiz.models import Proposicao, Parlamentar, CasaLegislativa, Votacao, Partido, Voto

class ProposicaoAdmin(admin.ModelAdmin):
    list_display = ('id_prop', 'ementa')
    search_fields = ('id_prop','ementa', 'hashtags')

class VotoAdmin(admin.TabularInline):
    model = Voto
    list_display = ('')

class ParlamentarAdmin(admin.ModelAdmin):
    list_display = ('nome','partido', 'situacao')
    search_fields = ('nome',)
    list_filter = ('partido', 'situacao')
    ordering = ('-situacao','nome')
    inlines = [VotoAdmin]

admin.site.register(Proposicao, ProposicaoAdmin)
admin.site.register(Parlamentar, ParlamentarAdmin)
admin.site.register(CasaLegislativa)
admin.site.register(Votacao)
admin.site.register(Partido)
admin.site.register(Voto)
