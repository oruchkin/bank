from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from django.db.models import Avg, Count, Min, Sum
from .models import Account, User
from .forms import Account_creation_Model_Form, Account_add_money_Model_Form
# Create your views here.


def index(request):
    all_users = User.objects.all()
    
    return render(request, "account/index.html",{
        "all_users": all_users,
    })


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "account/register.html", {
                "message": "Passwords must match."
            })
            
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "account/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "account/register.html")
    

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "account/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "account/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def profile(request, user_pk):    
    
    user_pk = User.objects.get(pk = user_pk)
    all_accounts = Account.objects.filter(account_owner=user_pk)
    how_much_money = Account.objects.filter(account_owner=user_pk).aggregate(Sum('money'))    
    
    page_owner = False
    if user_pk == request.user:
        page_owner =True
        
    print(page_owner)
    
    return render(request, "account/profile.html", {
        "user_pk": user_pk,
        "all_accounts":all_accounts,
        "how_much_money": how_much_money["money__sum"],
        "page_owner": page_owner,
    })

# ???????????????? ?????????? (???? ??????????????) (???? ???????????????? ??????????????)
def create_account(request):
    if request.method == "POST":
        form = Account_creation_Model_Form(request.POST)
        if form.is_valid():
            account_owner = request.user
            account_name = form.cleaned_data["account_name"]
            new_account = Account(account_owner=account_owner,account_name=account_name)
            new_account.save()
            
            user_pk = request.user.id
            return HttpResponseRedirect(reverse("profile", args=[user_pk]))
    
    else:
        user = request.user
        create_account = True
        form = Account_creation_Model_Form()

            
        return render(request, "account/profile.html", {
            "user": user,
            "create_account": create_account,
            "form": form,
            "all_accounts": Account.objects.filter(account_owner=user),
        })


# ?????????????? ????????
def delete_account(request, account_pk):
    object_to_delete = Account.objects.get(pk=account_pk)
    object_to_delete.delete()
    user_pk = request.user.id
    return HttpResponseRedirect(reverse("profile", args=[user_pk]))
    
    
# ???????????????? ???????????? ???? ????????
def add_money(request, account_pk):
    if request.method == "POST":
        form = Account_add_money_Model_Form(request.POST)
        if form.is_valid(): 
            change_money = form.cleaned_data["money"]
            money_account = Account.objects.get(pk=account_pk)
            old_money = money_account.money
            new_money = old_money + change_money
            
            money_account.money = new_money
            money_account.save()
            
            user_pk = request.user.id
            return HttpResponseRedirect(reverse("profile", args=[user_pk]))
            
    else:
        user = request.user
        add_money = True
        form = Account_add_money_Model_Form()
        return render(request, "account/profile.html", {
            "user": user,
            "add_money": add_money,
            "form": form,
            "all_accounts": Account.objects.filter(account_owner=user),
        })


def move_money(request, account_pk):
    current_account = Account.objects.filter(pk=account_pk).first()
    return render(request, "account/move_money.html",{
        "current_account": current_account,
    })
