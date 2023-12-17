import json
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseForbidden, HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist

from main.models import Book

from .models import Forum, ForumReply
from .forms import ForumForm, ForumReplyForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


@login_required(login_url=reverse_lazy('auths:login'))
def create_forum(request):
    # check if user role is READER
    if request.user.role != 'READER' and request.user.role != 'AUTHOR':
        return HttpResponseForbidden('FORBIDDEN')

    # create forum form
    form = ForumForm(request.POST or None)

    # if user upload form, then save form
    if form.is_valid() and request.method == 'POST':
        forum = form.save(commit=False)
        forum.forum_creator_id = request.user
        forum.save()

        return HttpResponseRedirect(reverse('forum:display_all_forum'))

    context = {'form': form, 'role': request.user.role}
    return render(request, "create_forum.html", context)


@login_required(login_url=reverse_lazy('auths:login'))
def display_all_forum(request):
    # return forbidden if user role is not READER
    if request.user.role != 'READER' and request.user.role != 'AUTHOR':
        return HttpResponseForbidden('FORBIDDEN')

    # get all forums from db
    forums = Forum.objects.all()
    print(forums)

    context = {'forums': forums, 'role': request.user.role}
    return render(request, 'all_forums.html', context)


@login_required(login_url=reverse_lazy('auths:login'))
def display_forum_by_id(request, forum_id):
    if request.user.role != 'READER' and request.user.role != 'AUTHOR':
        return HttpResponseForbidden('FORBIDDEN')

    forum = Forum.objects.get(pk=forum_id)
    replies = ForumReply.objects.filter(forum_id=forum_id)

    reply_form = ForumReplyForm(request.POST or None)

    if reply_form.is_valid() and request.method == 'POST':
        reply = reply_form.save(commit=False)
        reply.commentor_id = request.user
        reply.forum_id = forum
        forum.num_comments += 1
        forum.save()
        reply.save()
        # replies = ForumReply.objects.filter(forum_id=forum_id)

    context = {'forum': forum, 'replies': replies,
               'reply_form': reply_form, 'role': request.user.role}
    return render(request, 'forum_details.html', context)


# @login_required(login_url=reverse_lazy('auths:login'))
@csrf_exempt
def display_all_forums_ajax(request):
    print(request.COOKIES.get('sessionid'))
    print(request.user)
    try:
        if request.user.role != 'READER' and request.user.role != 'AUTHOR':
            return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)
    except:
        return JsonResponse({'message': 'Forbidden.', 'status': 403}, status=403)

    forums = Forum.objects.all()
    json_response = []

    for forum in forums:
        forum_json = {
            'forumDetailLink': f'/forum/{forum.forum_id}',
            'forumTitle': forum.forum_title,
            'book': {
                'cover': forum.book_topic.book_cover_link,
                'title': forum.book_topic.book_title
            },
            'creatorUsername': forum.forum_creator_id.username,
            'numberOfComments': forum.num_comments
        }

        json_response.append(forum_json)

    return JsonResponse({'forums': json_response, 'status': 200}, status=200)

    # forums = Forum.objects.all()

    # return HttpResponse(serializers.serialize("json", forums), content_type="application/json")


@login_required(login_url=reverse_lazy('auths:login'))
def display_forum_by_id_ajax(request, forum_id):
    if request.user.role != 'READER' and request.user.role != 'AUTHOR':
        return HttpResponseForbidden('FORBIDDEN')

    forum = Forum.objects.get(pk=forum_id)
    replies = ForumReply.objects.filter(forum_id=forum_id)

    reply_list_json = []

    for reply in replies:
        reply_list_json.append({
            'username': reply.commentor_id.username,
            'comment': reply.text
        })

    json_response = {
        'forumTitle': forum.forum_title,
        'book': {
            'cover': forum.book_topic.book_cover_link,
            'title': forum.book_topic.book_title
        },
        'creatorUsername': forum.forum_creator_id.username,
        'forumDiscussion': forum.forum_discussion,
        'numberOfComments': forum.num_comments,
        'replies': reply_list_json
    }

    return JsonResponse({'forum': json_response})


@login_required(login_url=reverse_lazy('auths:login'))
def add_reply_to_forum_ajax(request, forum_id):
    if request.user.role != 'READER' and request.user.role != 'AUTHOR':
        return HttpResponseForbidden('FORBIDDEN')

    if request.method == 'POST':
        comment = request.POST.get('comment')

        try:
            forum = Forum.objects.get(forum_id=forum_id)

            forum_reply = ForumReply(
                commentor_id=request.user, forum_id=forum, text=comment)
            forum_reply.save()
            return JsonResponse({'msg': 'Success!', 'reply': {'username': request.user.username, 'comment': comment}})
        except ObjectDoesNotExist:
            return Http404('NOT FOUND')

    else:
        return JsonResponse({'msg': 'BAD REQUEST'}, status=400)


@csrf_exempt
def create_forum_ajax(request):
    print(request.COOKIES.get('sessionid'))
    if request.user.role != 'READER' and request.user.role != 'AUTHOR':
        return JsonResponse({
            'message': 'Forbidden',
            'status': 403
        }, status=403)

    if request.method == 'POST':
        user = request.user

        print(user)

        data = json.loads(request.body)
        print(data)

        try:
            bookTopic = Book.objects.get(book_id=data['bookTopic'])
            Forum.objects.create(
                forum_title=data['title'], forum_discussion=data['discussion'], book_topic=bookTopic, forum_creator_id=user)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Book is not found.', 'status': 404}, status=404)
        except:
            return JsonResponse({'message': 'Internal server error', 'status': 500}, status=500)

        return JsonResponse({'message': 'Success created forum!', 'status': 200}, status=200)
    else:
        return JsonResponse({
            'message': 'BAD REQUEST',
            'status': 400
        }, status=400)
