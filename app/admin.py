from django.contrib import admin
from .models import * 

class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

class PessoaFisicaInline(admin.TabularInline):
    model = PessoaFisica
    extra = 1

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1
    fields = ('nome', 'carga_horaria_total', 'duracao_meses', 'area_saber') 

class DisciplinaCursoInline(admin.TabularInline):
    model = DisciplinaCurso
    extra = 1

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1

class UFAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [CidadeInline] 

class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [PessoaFisicaInline] 

class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'email')
    search_fields = ('nome', 'cidade__nome')
    inlines = [CursoInline] 

class AreaSaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [CursoInline] 

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'carga_horaria_total')
    list_filter = ('instituicao', 'area_saber')
    search_fields = ('nome',)
    inlines = [DisciplinaCursoInline] 

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'area_saber')
    search_fields = ('nome',)
    inlines = [AvaliacaoInline] 

class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turno', 'curso')
    list_filter = ('turno', 'curso')
    inlines = [MatriculaInline] 

admin.site.register(UF, UFAdmin)
admin.site.register(Ocupacao, OcupacaoAdmin)
admin.site.register(InstituicaoEnsino, InstituicaoEnsinoAdmin)
admin.site.register(AreaSaber, AreaSaberAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Turma, TurmaAdmin)

admin.site.register(Cidade) 
admin.site.register(Turno)
admin.site.register(PessoaFisica) 
admin.site.register(TipoAvaliacao)
admin.site.register(DisciplinaCurso)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Ocorrencia)

