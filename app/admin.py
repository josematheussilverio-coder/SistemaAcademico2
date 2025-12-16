from django.contrib import admin
from .models import * 

class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

class CadastroInline(admin.TabularInline):
    model = Cadastro
    extra = 1

class CursoInstituicaoInline(admin.TabularInline):
    model = Curso
    extra = 1
    fields = ('nome', 'carga_horaria_total', 'duracao_meses', 'area_saber') 

class CursoAreaSaberInline(admin.TabularInline):
    model = Curso
    extra = 1
    fields = ('nome', 'carga_horaria_total', 'duracao_meses', 'instituicao')

class DisciplinaCursoInline(admin.TabularInline):
    model = DisciplinaCurso
    extra = 1

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1

class FrequenciaPessoaInline(admin.TabularInline):
    model = Frequencia
    extra = 0 

class AvaliacaoPessoaInline(admin.TabularInline):
    model = Avaliacao
    extra = 0 



class UFAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [CidadeInline] 

class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [CadastroInline] 

class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'email')
    search_fields = ('nome', 'cidade__nome')
    inlines = [CursoInstituicaoInline] 

class AreaSaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [CursoAreaSaberInline] 

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

class PessoaFisicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'cidade', 'ocupacao')
    search_fields = ('nome', 'cpf')
    inlines = [FrequenciaPessoaInline, AvaliacaoPessoaInline] 


admin.site.register(UF, UFAdmin)
admin.site.register(Ocupacao, OcupacaoAdmin)
admin.site.register(InstituicaoEnsino, InstituicaoEnsinoAdmin)
admin.site.register(AreaSaber, AreaSaberAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Cadastro, PessoaFisicaAdmin) 

admin.site.register(Cidade) 
admin.site.register(Turno)
admin.site.register(TipoAvaliacao)
admin.site.register(DisciplinaCurso)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Ocorrencia)