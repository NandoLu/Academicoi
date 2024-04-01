"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', TemplateView.as_view(template_name='index.html'),name='index'),
    path('cidade/', CidadeView.as_view(), name='cidade'),
    path('ocupacao/', OcupacaoView.as_view(), name='ocupacao'),
    path('instituicao/', InstituicaoView.as_view(), name='instituicao'),
    path('areasaber/', AreasaberView.as_view(), name='areasaber'),
    path('curso/', CursoView.as_view(), name='curso'),
    path('periodo/', PeriodoView.as_view(), name='periodo'),
    path('disciplina/', DisciplinaView.as_view(), name='disciplina'),
    path('pessoa/', PessoaView.as_view(), name='pessoa'),
    path('matricula/', MatriculaView.as_view(), name='matricula'),
    path('avaliacao/', AvaliacaoTipoView.as_view(), name='avaliacao'),
    path('frequencia/', FrequenciaView.as_view(), name='frequencia'),
    path('turma/', TurmaView.as_view(), name='turma'),
    path('ocorrencia/', OcorrenciaView.as_view(), name='ocorrencia'),
    path('disciplinacurso/', DisciplinaView.as_view(), name='disciplinacurso'),
    path('avaliacaotipo/', AvaliacaoTipoView.as_view(), name='avaliacaotipo'),
]

