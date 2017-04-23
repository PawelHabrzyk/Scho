from django.shortcuts import render
from django.http import HttpResponse
from models import Post,NiemPost

def index(request):
    post_published = Post.objects.order_by('-data'[:5]),
    output = ', '.join([q.title for q in post_published])
    return HttpResponse(output)



def detail(request, post_id):
    return HttpResponse("patrzys na rozwiniecie Postu nr %s" % post_id)


