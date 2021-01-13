from django.shortcuts import render,redirect
from auction.models import Auction

def auctions(request):
    if not request.user.is_authenticated:
        return redirect('/signup')
    template = 'auction_app/auctions.html'
    context = {}
    objs = Auction.objects.filter(seller=request.user)
    context['auctions1'] = []
    context['auctions2'] = []
    for i in objs:
        if i.status == 1:
            context['auctions1'].append(i)
        else:
            context['auctions2'].append(i)
    return render(request,template,context)