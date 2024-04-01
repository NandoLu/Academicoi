from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View

class IndexView(View) :
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request) :
        pass
    
class CidadeView(View):
    def get(self, request, *args, **kwargs):
        cidade = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidade': cidade})

class OcupacaoView(View):
    def get(self, request, *args, **kwargs):
        ocupacao = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacao': ocupacao})

class InstituicaoView(View):
    def get(self, request, *args, **kwargs):
        instituicao = Instituicao.objects.all()
        return render(request, 'instituicao.html', {'instituicao': instituicao})
    
class AreasaberView(View):
    def get(self, request, *args, **kwargs):
        areasaber = Areasaber.objects.all()
        return render(request, 'areasaber.html', {'areasaber': areasaber})
    
class CursoView(View):
    def get(self, request, *args, **kwargs):
        curso = Curso.objects.all()
        return render(request, 'curso.html', {'curso': curso})
    
class PeriodoView(View):
    def get(self, request, *args, **kwargs):
        periodo = Periodo.objects.all()
        return render(request, 'periodo.html', {'periodo': periodo})
    
class DisciplinaView(View):
    def get(self, request, *args, **kwargs):
        disciplina = Disciplina.objects.all()
        return render(request, 'disciplina.html', {'disciplina': disciplina})
    
class PessoaView(View):
    def get(self, request, *args, **kwargs):
        pessoa = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoa': pessoa})
    
class MatriculaView(View):
    def get(self, request, *args, **kwargs):
        matricula = Matricula.objects.all()
        return render(request, 'matricula.html', {'matricula': matricula})
    
class AvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        avaliacao = Avaliacao.objects.all()
        return render(request, 'avaliacao.html', {'avaliacao': avaliacao})
    
class FrequenciaView(View):
    def get(self, request, *args, **kwargs):
        frequencia = Frequencia.objects.all()
        return render(request, 'frequencia.html', {'frequencia': frequencia})
    
class TurmaView(View):
    def get(self, request, *args, **kwargs):
        turma = Turma.objects.all()
        return render(request, 'turma.html', {'turma': turma})
    
class OcorrenciaView(View):
    def get(self, request, *args, **kwargs):
        ocorrencia = Ocorrencia.objects.all()
        return render(request, 'ocorrencia.html', {'ocorrencia': ocorrencia})
    
class DisciplinaCursoView(View):
    def get(self, request, *args, **kwargs):
        disciplinacurso = Disciplina_curso.objects.all()
        return render(request, 'disciplina curso.html', {'disciplinacurso': disciplinacurso})
    
class AvaliacaoTipoView(View):
    def get(self, request, *args, **kwargs):
        avaliacaotipo = Avaliacao_tipo.objects.all()
        return render(request, 'avaliacao tipo.html', {'avaliacaotipo': avaliacaotipo})
