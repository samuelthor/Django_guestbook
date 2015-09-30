from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import text



def index(request):
    latest_question_list = text.objects.order_by('-pub_date')[:50]
    print (latest_question_list)
    length = []
    for i in latest_question_list:
        length.append(len(i.question_text))

    context = {'latest_question_list': latest_question_list,
        'length': length,
    }
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        q = text(title_text=request.POST['titill'], pub_date=timezone.now(),question_text=request.POST['txtArea'])
        q.save()
    return render(request, 'guestbook/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(text, pk=question_id)
    context = {
        'question': question,
        'previous':int(question_id) - 1,
        'next':int(question_id) + 1,
    }
    return render(request, 'guestbook/detail.html', context)

def create(request):
    # if this is a POST request we need to process the form data



    return render(request, 'guestbook/create.html')











"""
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
"""
