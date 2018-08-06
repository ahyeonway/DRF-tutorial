from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Snippet
from .serializers.ModelSerializer import SnippetSerializer


def snippet_list(request):
    snippets = Snippet.objects.all()
    serializer = SnippetSerializer(snippets, many=True)

    return HttpResponse(serializer.data)