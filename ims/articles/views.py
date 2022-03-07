from django.shortcuts import render
from .models import Article

# Create your views here.
def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = { "object": article_obj }
    return render(request, "articles/detail.html", context=context)

def article_search_view(request):
    #print(dir(request))
    query_dict = request.GET #this is a dictionary
    query = query_dict.get("q") #<input type="text" name="q"  />
    article_obj = None #setting a default value of none to article
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        "object": article_obj
    }
    return render(request,"articles/search.html",context=context)