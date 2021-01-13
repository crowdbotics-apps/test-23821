from django.shortcuts import render,HttpResponse
from .models import notification_model,notification_pref

def notification_page(request):
    template = 'notification_app/notification.html'
    context = {}
    objs = notification_model.objects.filter(user=request.user)
    temp_dic = {}
    for i in reversed(objs):
        try:
            temp_dic[i.date].append(i)
        except:
            temp_dic[i.date] = [i]
    context['notifications'] = temp_dic
    try:
        context['pref'] = notification_pref.objects.get(user=request.user)
    except:
        obj = notification_pref()
        obj.user = request.user
        obj.save()
        context['pref'] = obj
    return render(request,template,context)

def preference_submit(request):
    objp = notification_pref.objects.get(user=request.user)
    try:
        if request.POST['rfs_daily'] == 'on':
            objp.rfs_daily = True
            objp.save()
    except:
        objp.rfs_daily = False
        objp.save()
    try:
        if request.POST['rfs_week'] == 'on':
            objp.rfs_week = True
            objp.save()
    except:
        objp.rfs_week = False
        objp.save()
    try:
        if request.POST['comment_mention'] == 'on':
            objp.comment_mention = True
            objp.save()
    except:
        objp.comment_mention = False
        objp.save()
    try:
        if request.POST['comment_reply'] == 'on':
            objp.comment_reply = True
            objp.save()
    except:
        objp.comment_reply = False
        objp.save()
    try:
        if request.POST['play_sound'] == 'on':
            objp.play_sound = True
            objp.save()
    except:
        objp.play_sound = False
        objp.save()
    try:
        if request.POST['before_auction'] == 'on':
            objp.before_auction = True
            objp.save()
    except:
        objp.before_auction = False
        objp.save()
    try:
        if request.POST['new_bids'] == 'on':
            objp.new_bids = True
            objp.save()
    except:
        objp.new_bids = False
        objp.save()
    try:
        if request.POST['new_comments'] == 'on':
            objp.new_comments = True
            objp.save()
    except:
        objp.new_comments = False
        objp.save()
    try:
        if request.POST['questions_answered'] == 'on':
            objp.questions_answered = True
            objp.save()
    except:
        objp.questions_answered = False
        objp.save()
    try:
        if request.POST['auction_results'] == 'on':
            objp.auction_results = True
            objp.save()
    except:
        objp.auction_results = False
        objp.save()
    return HttpResponse('done')