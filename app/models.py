from django.db import models

class UF(models.Model):
    nome = models.CharField(max_length=2, unique=True, verbose_name="UF")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "UF"
        verbose_name_plural = "UFs"
        ordering = ['nome']

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    uf = models.ForeignKey(UF, on_delete=models.PROTECT, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}/{self.uf.nome}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        unique_together = ('nome', 'uf')
        ordering = ['nome']

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"
        ordering = ['nome']

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Área do Saber"
        verbose_name_plural = "Áreas do Saber"
        ordering = ['nome']

class Turno(models.Model):
    nome = models.CharField(max_length=50, unique=True, verbose_name="Nome")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"
        ordering = ['nome']

class TipoAvaliacao(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Tipo de Avaliação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Avaliação"
        verbose_name_plural = "Tipos de Avaliação"
        ordering = ['nome']

class Pessoa(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome Completo")
    nome_do_pai = models.CharField(max_length=255, verbose_name="Nome do Pai")
    nome_da_mae = models.CharField(max_length=255, verbose_name="Nome da Mãe")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF") # Adicionado formatação de CPF
    data_nasc = models.DateField(verbose_name="Data de Nascimento")
    email = models.EmailField(verbose_name="E-mail")

    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.PROTECT, verbose_name="Ocupação")

    class Meta:
        abstract = True 
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Cadastro(Pessoa):
    class Meta:
        verbose_name = "Cadastro"
        verbose_name_plural = "Cadastros"

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")
    site = models.URLField(max_length=200, null=True, blank=True, verbose_name="Site")
    email = models.EmailField(verbose_name="E-mail")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, verbose_name="Cidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Instituição de Ensino"
        verbose_name_plural = "Instituições de Ensino"
        ordering = ['nome']

class Disciplina(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.PROTECT, verbose_name="Área do Saber")

    def __str__(self):
        return f"{self.nome} ({self.area_saber.nome})"

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"
        ordering = ['nome']

class Curso(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")
    carga_horaria_total = models.IntegerField(verbose_name="Carga Horária Total (horas)")
    duracao_meses = models.IntegerField(verbose_name="Duração (meses)")

    area_saber = models.ForeignKey(AreaSaber, on_delete=models.PROTECT, verbose_name="Área do Saber")
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.PROTECT, verbose_name="Instituição")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['nome']

class DisciplinaCurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, verbose_name="Disciplina")
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT, verbose_name="Turno")
    carga_horaria = models.IntegerField(verbose_name="Carga Horária (h)")

    def __str__(self):
        return f"{self.disciplina.nome} em {self.curso.nome} ({self.turno.nome})"

    class Meta:
        verbose_name = "Disciplina por Curso"
        verbose_name_plural = "Disciplinas por Curso"
        unique_together = ('curso', 'disciplina')
        ordering = ['curso', 'disciplina']

class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Turma")
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT, verbose_name="Turno")
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso") 

    def __str__(self):
        return f"{self.nome} ({self.turno.nome})"

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
        ordering = ['nome']


class Matricula(models.Model):
    pessoa = models.ForeignKey(Cadastro, on_delete=models.PROTECT, verbose_name="Pessoa (Estudante)")
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso")
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT, verbose_name="Turma") 
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_previsao_termino = models.DateField(verbose_name="Previsão de Término")
    
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.PROTECT, verbose_name="Instituição")

    def __str__(self):
        return f"Matrícula de {self.pessoa.nome} em {self.curso.nome}"

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"
        unique_together = ('pessoa', 'curso') 
        ordering = ['pessoa']

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="Descrição da Avaliação")
    nota = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Nota Obtida", null=True, blank=True)

    tipoavaliacao = models.ForeignKey(TipoAvaliacao, on_delete=models.PROTECT, verbose_name="Tipo de Avaliação")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Cadastro, on_delete=models.PROTECT, verbose_name="Pessoa Avaliada") 
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso") 

    def __str__(self):
        return f"{self.descricao} - {self.disciplina.nome}"

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        ordering = ['disciplina', 'pessoa']

class Frequencia(models.Model):
    data = models.DateField(verbose_name="Data da Aula")
    numero_faltas = models.IntegerField(verbose_name="Número de Faltas")
    
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Cadastro, on_delete=models.PROTECT, verbose_name="Pessoa (Aluno)") # Quem faltou
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso") # Adicionado para contexto

    def __str__(self):
        return f"Frequência de {self.pessoa.nome} em {self.disciplina.nome}"

    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"
        ordering = ['data', 'disciplina']

class Ocorrencia(models.Model):
    descricao = models.TextField(verbose_name="Descrição da Ocorrência")
    data = models.DateField(auto_now_add=True, verbose_name="Data do Registro")
    
    pessoa = models.ForeignKey(Cadastro, on_delete=models.PROTECT, verbose_name="Pessoa Envolvida")
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso", null=True, blank=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, verbose_name="Disciplina", null=True, blank=True)

    def __str__(self):
        return f"Ocorrência de {self.pessoa.nome} em {self.data}"

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"
        ordering = ['-data']
