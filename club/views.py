from django.core.paginator import Paginator
from club.forms import MemberForm
from club.models import Member
from django.shortcuts import redirect, render
import re
# Create your views here.

def member_list(request):
    context = {}
    members = Member.objects.filter(generation__gt=11).order_by('-generation')
    paginator = Paginator(members, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request=request, template_name='club/list.html', context=context)

def member_create(request):
    context = {}
    form = MemberForm(request.POST, request.FILES)
    if form.is_valid():

        Member.objects.create(**form.cleaned_data)
        return redirect('club:member_list')

    context["form"] = form
    return render(request, "club/create.html", context)

def member_read(request, pk):
    member = Member.objects.get(pk=pk)
    context = {"member": member}
    return render(request=request, template_name='club/read.html', context=context)

def member_update(request, pk):
    context = {}
    if request.method == "POST":
        form = MemberForm(request.POST, request.FILES)
        member = Member.objects.get(pk=pk)
        if form.is_valid():
            member.generation = form.cleaned_data["generation"]
            member.birth_date = form.cleaned_data["birth_date"]
            member.email = form.cleaned_data["email"]
            cleaned_phone_number = form.cleaned_data["phone_number"]
            if re.match(r"(\d+){11}", cleaned_phone_number):
                member.phone_number = f"{cleaned_phone_number[:3]}-{cleaned_phone_number[3:7]}-{cleaned_phone_number[7:11]}"
            else:
                member.phone_number = cleaned_phone_number
            member.profile = form.cleaned_data.get("profile")
            member.introduction = form.cleaned_data.get("introduction")
            member.save()

        return redirect('club:member_read', pk=member.pk)

    elif request.method == "GET":
        member = Member.objects.get(pk=pk)
        form = MemberForm(instance=member)
        context["form"] = form
        context["member"] = member
        return render(request, "club/update.html", context)

def member_delete(request, pk):
    if request.method == "POST":
        member = Member.objects.get(pk=pk)
        member.delete()
    return redirect('club:member_list')
