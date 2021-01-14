from django.shortcuts import render,redirect
import requests,json
from proud_forest_23287.settings import MAILCHIMP_API_KEY,MAILCHIMP_USERNAME
from mailchimp3 import MailChimp

from django.contrib.auth.decorators import login_required

@login_required
def newsletter_signup(request):
    template = 'newsletter_app/signup.html'
    context = {}
    if request.method == 'POST':
        client = MailChimp(mc_api=MAILCHIMP_API_KEY,mc_user=MAILCHIMP_USERNAME)
        tempa = client.lists.all(get_all=True,fields='lists.id')
        tempb = tempa['lists'][0]['id']
        tempc = client.lists.members.create(tempb,{'email_address':request.POST['email'],'status':'subscribed'})
        return redirect('/newsletter-signup-complete')
    return render(request,template,context)

def signup_complete(request):
    template = 'newsletter_app/complete.html'
    context = {}
    return render(request,template,context)
