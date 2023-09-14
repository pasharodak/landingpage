from django.shortcuts import render
from django.http import HttpResponse
from .forms import Orderform
from cms.models import CmsSlider
from price.models import PriceCard,PriceTable
from .models import Order
from telebot.models import SettingTg
import requests

# Create your views here.
def new_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    pt_list = PriceTable.objects.all()
    form = Orderform()
    dict_odj = {'slider_list':slider_list,
                'pc_1':pc_1,
                'pc_2':pc_2,
                'pc_3':pc_3,
                'pt_list':pt_list,
                "form":form}
    return render(request,'./index.html',dict_odj)


def thanks_page(request):
    name = request.POST["name"]
    phone = request.POST["phone"]
    element = Order(order_name=name,order_phone=phone)
    element.save()
    pk_1 = SettingTg.objects.get(pk=1)
    api = "https://api.telegram.org/bot"
    token = str(pk_1.st_token)
    chat_id = str(pk_1.st_id_group)
    text = str(pk_1.st_text) + f"\n {name} \n {phone}"
    method = api + token + "/sendMessage"
    req = requests.post(method, data={
        "chat_id": chat_id,
        "text": text
    })
    return render(request, "./thanks.html", {"name":name,"phone":phone})