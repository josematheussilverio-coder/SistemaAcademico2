from django.shortcuts import render
from django.views import View
from .models import *
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import *


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
    
class CursosView(View):
    def get(self, request):
        cursos = Curso.objects.all()
        return render(request, 'cursos.html', {'cursos': cursos})
    

class CursoCreate(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso_form.html'
    success_url = reverse_lazy('cursos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Novo Curso"
        return context

class CursoUpdate(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso_form.html'
    success_url = reverse_lazy('cursos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Curso"
        return context

class CursoDelete(DeleteView):
    model = Curso
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('cursos')

class DisciplinasView(View):
    def get(self, request):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplinas.html', {'disciplinas': disciplinas})

class TurmasView(View):
    def get(self, request):
        turmas = Turma.objects.all()
        return render(request, 'turmas.html', {'turmas': turmas})
    
class TurmaCreate(CreateView):
    model = Turma
    form_class = TurmaForm
    template_name = 'turma_form.html'
    success_url = reverse_lazy('turmas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nova Turma"
        return context

class TurmaUpdate(UpdateView):
    model = Turma
    form_class = TurmaForm
    template_name = 'turma_form.html'
    success_url = reverse_lazy('turmas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Turma"
        return context

class TurmaDelete(DeleteView):
    model = Turma
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('turmas')

class CadastroView(View):
    def get(self, request):
        cadastros = Cadastro.objects.all()
        return render(request, 'cadastros.html', {'cadastros': cadastros})
    
class CadastroCreate(CreateView):
    model = Cadastro
    form_class = CadastroForm
    template_name = 'cadastro_form.html'
    success_url = reverse_lazy('cadastros')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Novo Cadastro"
        return context
    
class CadastroUpdate(UpdateView):
    model = Cadastro
    form_class = CadastroForm
    template_name = 'cadastro_form.html'
    success_url = reverse_lazy('cadastros')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Cadastro"
        return context
    
class CadastroDelete(DeleteView):
    model = Cadastro
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('cadastros')
    

class InstituicoesView(View):
    def get(self, request):
        instituicoes = InstituicaoEnsino.objects.all()
        return render(request, 'instituicoes.html', {'instituicoes': instituicoes})

class AreasView(View):
    def get(self, request):
        areas = AreaSaber.objects.all()
        return render(request, 'areas.html', {'areas': areas})

class CidadesView(View):
    def get(self, request):
        cidades = Cidade.objects.all()
        return render(request, 'cidades.html', {'cidades': cidades})

class MatriculasView(View):
    def get(self, request):
        matriculas = Matricula.objects.all()
        return render(request, 'matriculas.html', {'matriculas': matriculas})
    

class MatriculaCreate(CreateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'matricula_form.html'
    success_url = reverse_lazy('matriculas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nova Matrícula"
        return context

class MatriculaUpdate(UpdateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'matricula_form.html'
    success_url = reverse_lazy('matriculas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Matrícula"
        return context

class MatriculaDelete(DeleteView):
    model = Matricula
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('matriculas')


class OcorrenciasView(View):
    def get(self, request):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencias.html', {'ocorrencias': ocorrencias})

class OcorrenciaCreate(CreateView):
    model = Ocorrencia
    form_class = OcorrenciaForm
    template_name = 'ocorrencia_form.html'
    success_url = reverse_lazy('ocorrencias')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nova Ocorrência"
        return context

class OcorrenciaUpdate(UpdateView):
    model = Ocorrencia
    form_class = OcorrenciaForm
    template_name = 'ocorrencia_form.html'
    success_url = reverse_lazy('ocorrencias')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Ocorrência"
        return context

class OcorrenciaDelete(DeleteView):
    model = Ocorrencia
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('ocorrencias')


class FrequenciasView(View):
    def get(self, request):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencias.html', {'frequencias': frequencias})

class FrequenciaCreate(CreateView):
    model = Frequencia
    form_class = FrequenciaForm
    template_name = 'frequencia_form.html'
    success_url = reverse_lazy('frequencias')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Registrar Faltas"
        return context

class FrequenciaUpdate(UpdateView):
    model = Frequencia
    form_class = FrequenciaForm
    template_name = 'frequencia_form.html'
    success_url = reverse_lazy('frequencias')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Frequência"
        return context

class FrequenciaDelete(DeleteView):
    model = Frequencia
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('frequencias')


class AvaliacoesView(View):
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes})

class AvaliacaoCreate(CreateView):
    model = Avaliacao
    form_class = AvaliacaoForm
    template_name = 'avaliacao_form.html'
    success_url = reverse_lazy('avaliacoes')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Lançar Nota"
        return context

class AvaliacaoUpdate(UpdateView):
    model = Avaliacao
    form_class = AvaliacaoForm
    template_name = 'avaliacao_form.html'
    success_url = reverse_lazy('avaliacoes')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Nota"
        return context

class AvaliacaoDelete(DeleteView):
    model = Avaliacao
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('avaliacoes')
    
