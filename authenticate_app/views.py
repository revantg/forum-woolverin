from django.shortcuts import redirect
from django.shortcuts import render
from authenticate_app.forms import threadForm, replyForm
from authenticate_app.models import thread, reply
from django.http import HttpResponse
from random import randint as RI


def display_all_threads(request):
    threads = thread.objects.order_by('datetime')
    print(threads)
    data = []
    for i in threads:
        no_of_reply = (len(reply.objects.filter(parent_post_id = i.id)))
        temp = {"thread_data":i, "num_of_reply" : no_of_reply}
        data.append(temp)
    print(no_of_reply)
    all_threads = {'threads': threads,
                    'data' : data,
                    'title' : "All Threads",
                    'no_of_reply' : no_of_reply}
    return render(request, 'index.html', all_threads)


def view_thread(request, id):
    replies = reply.objects.filter(parent_post_id = id)
    all_threads = thread.objects.order_by('datetime')
    thread_data = thread.objects.get(id = id)
    reply_data = {"reply_data" : replies,
                  "thread_data": thread_data,
                  "all_threads": all_threads,
                  "random_img" : "/static/images/avatar{}.jpg".format(RI(1,4)),
                  "title"      : "View Thread",
                  "ide"        : id
                  }

    if request.method == "POST":
        replyform_data = replyForm(data=request.POST)
        replyform_data.parent_post_id = id
        # replyform_data.save()

        if replyform_data.is_valid():
            replyform_data.save()
        else:
            return HttpResponse("Unsucessful")
    return render(request, 'thread.html', reply_data)


def createthread(request):
    all_threads = thread.objects.order_by('datetime')
    threaddict = {
                    "all_threads" : all_threads,
                    "title"       : "Create Thread"
                }

    if request.method == "POST":
        form_data = threadForm(data = request.POST)
        if form_data.is_valid():
            form_data.save()
        else:
            print(form_data)
            return HttpResponse("Unsucessful")

    return render(request, 'createthread.html', threaddict)

def upthread(request, id):
    thread_data = thread.objects.get(id = id)
    print("\n\n", thread_data.likes, "\n\n\n")
    thread_data.likes += 1
    thread_data.save()
    return view_thread(request, id)

def downthread(request, id):
    thread_data = thread.objects.get(id = id)
    thread_data.dislikes += 1
    thread_data.save()
    return redirect('/forum/view/' + str(id))

def upreply(request, id):
    reply_data = reply.objects.get(id = id)
    reply_data.likes += 1
    reply_data.save()
    return redirect('/forum/view/' + str(reply_data.parent_post_id))


def downreply(request, id):
    reply_data = reply.objects.get(id=id)
    reply_data.dislikes += 1
    reply_data.save()
    return redirect('/forum/view/' + str(reply_data.parent_post_id))

