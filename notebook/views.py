from django.shortcuts import render

from .models import Note
from .documents import NoteDocument

from elasticsearch_dsl.query import MultiMatch, MoreLikeThis

# Create your views here.


def search(request):
    query = request.GET.get('q')
    # q = MultiMatch(query=query, fields=['title', 'body'])

    data = {
        'query':True,
        'more': NoteDocument.search().query(MoreLikeThis(like=query, fields=['title', 'body'])),
        'page': NoteDocument.search()
                .query('multi_match', query=query, fields=['title', 'body'])
                # .query("match", body=query)
    }
    # print(data['page'])
    for k in data['more']:
        print(k.body)
        print(k.title)
    return render(request, 'search/search.html', context=data)
