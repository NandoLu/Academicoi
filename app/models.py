from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da pessoa")
    uf = models.CharField(max_length=100, verbose_name="Nome do pai")

    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da ocupacao")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Ocupacao"
        verbose_name_plural = "Ocupacao"
        
class Instituicao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Instituicao")
    site = models.CharField(max_length=100, verbose_name="Site da Instituicao")
    telefone = models.CharField(max_length=100, verbose_name="Telefone da Instituicao")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da Instituicao")
    def __str__(self):
        return f"{self.nome}, {self.telefone}, {self.cidade}"
    class Meta:
        verbose_name = "Ocupacao"
        verbose_name_plural = "Ocupacao"
        
class Areasaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da area do saber")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Area do saber"
        verbose_name_plural = "Areas do saber"
        
class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da area do saber")
    carga_horaria = models.IntegerField(verbose_name="carga horaria")
    duracao_meses = models.IntegerField(verbose_name="duracao de meses")
    area = models.ForeignKey(Areasaber, on_delete=models.CASCADE, verbose_name="Area saber")
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituicao")
    
    def __str__(self):
        return f"{self.nome}, {self.carga_horaria}, {self.duracao_meses}"
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "cursos"
        
class Periodo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do período")
    
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"
        
class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da disciplina")
    area = models.ForeignKey(Areasaber, on_delete=models.CASCADE, verbose_name="Area saber")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nome do curso")
    
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"
        

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da pessoa")
    pai = models.CharField(max_length=100, verbose_name="Nome do pai")
    mae = models.CharField(max_length=100, verbose_name="Nome da mãe")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF da pessoa")
    data_nasci = models.DateField(verbose_name="Data de nascimento")
    email = models.CharField(max_length=100, verbose_name="email da pessoa")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da pessoa")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupacao da pessoa")

    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Nome da instituicoa")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nome do curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Nome da pessoa")
    data_inicio = models.DateField(verbose_name="Data de inicio")
    data_termino = models.DateField(verbose_name="Data prevista do termino")
    
    def __str__(self):
        return f"{self.instituicao}, {self.curso}, {self.pessoa}, {self.data_inicio}, {self.data_termino}"
    class Meta:
        verbose_name = "Matricula"
        verbose_name_plural = "Matriculas"
        
class Avaliacao(models.Model):
    descricao = models.CharField(max_length=200, verbose_name="Descricao da avaliacao")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nome do curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Nome da disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Nome da pessoa")
    
    def __str__(self):
        return f"{self.descricao}, {self.curso}, {self.pessoa}"
    class Meta:
        verbose_name = "Avaliacao"
        verbose_name_plural = "Avaliacoes"
        
class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nome do curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Nome da disciplina")
    numero_faltas = models.IntegerField(verbose_name = "Numero de faltas")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Nome da pessoa")
    
    def __str__(self):
        return f"{self.numero_faltas} {self.pessoa}"
    class Meta:
        verbose_name = "Falta"
        verbose_name_plural = "Faltas"
        
class Turma(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome da turma")
    periodo = models.CharField(verbose_name = "Nome do período")

    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Turma"
        verbose_name = "Turmas"
        
class Ocorrencia(models.Model):
    descricao = models.CharField(max_length = 100, verbose_name = "Descrição da ocorrencia")
    data = models.DateTimeField(verbose_name = "Data da ocorrencia")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nome do curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Nome do curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Nome da pessoa")

class Disciplina_curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da disciplina")
    carga_horaria = models.IntegerField(verbose_name="carga horaria da disciplina")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nome do curso")
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, verbose_name="Periodo da disciplina")
    
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"
        
class Avaliacao_tipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo da avalicao")
    
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Avaliacao"
        verbose_name_plural = "Avaliacoes"