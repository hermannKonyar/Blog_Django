from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from . models import BlogEntry,FoodBlog,UserInfo,Videos,About
import requests

# Create your views here.

data = {
    "blogs": [
        {
            'id': 1,
            'title': 'Ege Yöresi Yemekleri',
            'image': '5.jpg',
            'isActive': True,
            'isHome': True,
            'Description': 'İzmir Köfteasdasdasdasdasdsaasdasdasdasdasdasdasdasdasdasdasdasdasddsadasdasdasdasd'
        },
        {
            'id': 2,
            'title': 'Karadeniz Yöresi Yemekleri',
            'image': '6.jpg',
            'isActive': True,
            'isHome': True,
            'Description': 'Hamzi Pilavı'
        },
        {
            'id': 3,
            'title': 'Balkan Yemekleri',
            'image': '7.jpg',
            'isActive': True,
            'isHome': True,
            'Description': 'Trileçe'
        },
        {
            'id': 4,
            'title': 'Komple Veri Geliştirme',
            'image': 'foto1.jpg',
            'isActive': False,
            'isHome': True,
            'Description': 'Güzel Kurs'
        }
    ]
}
def index(request):
    about=About.objects.all()
    blogs=BlogEntry.objects.all().order_by('-id')[:3]
    return render(request, "blog/index.html",{
        'blogs':blogs,
        'about':about,
    })


def blogs(request):
    blog=BlogEntry.objects.all()
    p=Paginator(blog,4)
    page=request.GET.get('page')
    contexts=p.get_page(page)
    return render(request, "blog/blogs.html", {
        "blogs":blog,
        "contexts":contexts,
    })


def blog_details(request, id):
    blog=BlogEntry.objects.get(id=id)
    
    
    return render(request, "blog/blogs-details.html", {
        'blogs': blog,
    })

# def tarifler(request):
    
#     blog=BlogEntry.objects.all()
#     p=Paginator(blog,2)
#     page=request.GET.get('page')
#     contexts=p.get_page(page)
#     return render(request, "blog/tarifler.html", {
#         "blogs":blog,
#         "contexts":contexts,
#     })
    

# def tarifler_details(request,id):
#     blogs=data['blogs']
#     selectedBlog=None
    
    
    
    
#     for blog in blogs:
#         if blog['id']==id:
#             selectedBlog=blog
    
#     return render(request, "blog/blogs-details.html", {
#         'blogs': blogs,
#     })

def hakkimda(request):
    blog=About.objects.all().order_by('-id')[:1]
    return render(request,"blog/about.html"
                  ,{'blogs':blog})
