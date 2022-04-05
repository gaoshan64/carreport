from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.views.decorators.http import require_POST
from .models import ReportsContent,CarAbout,Customer,User,ReportsContent2,ReportsContent1
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required,permission_required
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomerAddForm,CarAboutForm,Report2ContentForm,Report1ContentForm
# Create your views here.

#SVG
#查看车辆报告


def hello_world(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def base_test(request):
    return render(request,'./base.html')

def index(request):
    reports=ReportsContent.objects.all()

    return render(request,'./index.html',{"reports":reports})

def report_list(request):
    reports = ReportsContent.objects.all()
    return render(request, './report_list.html', {"reports": reports})

@login_required(login_url='/account/login')
@permission_required('report_OA.view_customer',login_url='/account/login')
def customer_list(request):
    for_go_back=request.GET.dict()
    customers = Customer.objects.all()
    if request.GET.get('input_data'):
        if request.GET.get("w_col") == 'c_name':
            customers=Customer.objects.filter(c_name__contains=request.GET.get('input_data'))
        elif request.GET.get("w_col") == 'c_tel':
            customers = Customer.objects.filter(c_tel__contains=request.GET.get('input_data'))
        elif request.GET.get("w_col") == 'memo':
            customers = Customer.objects.filter(memo__contains=request.GET.get('input_data'))
        elif request.GET.get("w_col") == 'c_wechat':
            customers = Customer.objects.filter(c_wechat__contains=request.GET.get('input_data'))
    paginator=Paginator(customers,10)
    page = request.GET.get('page')
    try:
        current_page=paginator.page(page)
        customers =current_page.object_list
    except PageNotAnInteger:
        current_page=paginator.page(1)
        customers = current_page.object_list
    except EmptyPage:
        current_page=paginator.page(paginator.num_pages)
        customers = current_page.object_list
    return render(request,'./customers_list.html',{"customers":customers,"page":current_page,"for_go_back":for_go_back})

@login_required(login_url='/account/login')
@permission_required('report_OA.view_customer',login_url='/account/login')
def customer_detial(request,customer_id):
    customer=get_object_or_404(Customer,id=customer_id)




    return render(request,'./customer_detial.html',{"customer":customer})


@login_required(login_url='/account/login')
@permission_required('report_OA.add_customer',login_url='/account/login')
def customer_add(request):
    if request.method=="POST":
        customer_add_form = CustomerAddForm(data=request.POST)
        if customer_add_form.is_valid():
            cd = customer_add_form.cleaned_data
            try:
                new_customer= customer_add_form.save()
                return redirect('/customer_detial/{}'.format(new_customer.id))
            except Exception as e:
                return HttpResponse(e)
        else:
            #print(customer_add_form.errors)
            return render(request, "./customer_add.html",{"form":customer_add_form})
    else:
        customer_add_form = CustomerAddForm()

        return render(request, "./customer_add.html",{"form":customer_add_form})


@login_required(login_url='/account/login')
@permission_required('report_OA.delete_customer',login_url='/account/login')
@require_POST
def customer_del(request):
    customer_id = request.POST['customer_id']
    try:
        customer = Customer.objects.get(id=customer_id)
        customer.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("1")


@login_required(login_url='/account/login')
@permission_required('report_OA.change_customer',login_url='/account/login')
def customer_redit(request,customer_id):
    customer = Customer.objects.get(id=customer_id)
    if request.method == "GET":
        customer_form=CustomerAddForm(instance=customer)
        return render(request, "./customer_add.html",{"form":customer_form,"customer":customer})
    else:
        customer_form=CustomerAddForm(data=request.POST,instance=customer)
        if customer_form.is_valid():
            customer_form.save()
        else:
            return render(request, "./customer_add.html", {"form": customer_form, "customer": customer})
        return redirect('/customer_detial/{}'.format(customer_id))


    # customer = Customer.objects.get(id=customer_id)
    # customer_form = CustomerAddForm(
    #     initial={"c_name": customer.c_name,
    #              "c_tel": customer.c_tel,
    #              "memo": customer.memo,
    #              "c_wechat": customer.c_wechat}
    # )
    #
    # if request.method == "GET":
    #
    #     return render(request, "./customer_add.html",{"form":customer_form,"customer":customer})
    # else:
    #     customer_redit_form = CustomerAddForm(data=request.POST)
    #     if customer_redit_form.is_valid():
    #         form_cd=customer_redit_form.cleaned_data
    #         customer.c_name=form_cd['c_name']
    #         customer.c_tel=form_cd['c_tel']
    #         customer.c_wechat=form_cd['c_wechat']
    #         customer.memo=form_cd['memo']
    #         customer.save()
    #     else:
    #
    #         return render(request, "./customer_add.html", {"form": customer_form, "customer": customer})
    #     return  redirect('/customer_detial/{}'.format(customer_id))



@login_required(login_url='/account/login')
@permission_required('report_OA.view_carabout',login_url='/account/login')
def car_list(request):
    customer_id=request.GET.get('customer_id')
    cars=CarAbout.objects.all()
    if request.GET.get('input_data'):
        if request.GET.get("w_col") == 'car_brand_model':
            cars=CarAbout.objects.filter(car_brand_model__contains=request.GET.get('input_data'))
        elif request.GET.get("w_col") == 'car_license_tag_number':
            cars = CarAbout.objects.filter(car_license_tag_number__contains=request.GET.get('input_data'))
        elif request.GET.get("w_col") == 'car_id':
            cars = CarAbout.objects.filter(car_id__contains=request.GET.get('input_data'))
    if request.GET.get('customer_id'):
        cars=CarAbout.objects.filter(customer_id=request.GET.get('customer_id'))
    if request.GET.get('check_state'):
        cars=CarAbout.objects.filter(check_state='wait')

    paginator=Paginator(cars,10)
    page = request.GET.get('page')
    try:
        current_page=paginator.page(page)
        cars =current_page.object_list
    except PageNotAnInteger:
        current_page=paginator.page(1)
        cars = current_page.object_list
    except EmptyPage:
        current_page=paginator.page(paginator.num_pages)
        cars = current_page.object_list
    return render(request,'./car_list.html',{"cars":cars,"page":current_page,"customer_id":customer_id})

@login_required(login_url='/account/login')
@permission_required('report_OA.view_carabout',login_url='/account/login')
def car_detial(request,car_id):
    car=get_object_or_404(CarAbout,id=car_id)
    return render(request,'./car_detial.html',{"car":car})


@login_required(login_url='/account/login')
@permission_required('report_OA.del_carabout',login_url='/account/login')
@require_POST
def car_del(request):
    car_id = request.POST['car_id']
    try:
        car = CarAbout.objects.get(id=car_id)
        car.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("1")


@login_required(login_url='/account/login')
@permission_required('report_OA.add_carabout',login_url='/account/login')
def car_add(request):
    if request.method=="POST":
        car_add_form = CarAboutForm(data=request.POST)
        if car_add_form.is_valid():
            cd = car_add_form.cleaned_data
            try:
                new_car= car_add_form.save()
                return redirect('/car_detial/{}'.format(new_car.id))
            except:
                return HttpResponse("2")
        else:
            return render(request, "./car_add.html",{"form":car_add_form})
    else:
        customer_id=request.GET.get('customer_id')

        car_add_form = CarAboutForm(initial={"customer":customer_id})

        return render(request, "./car_add.html",{"form":car_add_form})


@login_required(login_url='/account/login')
@permission_required('report_OA.change_carabout',login_url='/account/login')
def car_redit(request,car_id):
    car = CarAbout.objects.get(id=car_id)

    if request.method == "GET":
        car_form = CarAboutForm(instance=car)
        return render(request, "./car_add.html",{"form":car_form,"car":car})
    else:
        car_form = CarAboutForm(data=request.POST,instance=car)
        if car_form.is_valid():
            car_form.save()
        else:
            return render(request, "./car_add.html", {"form": car_form, "car": car})

        return  redirect('/car_detial/{}'.format(car_id))

@login_required(login_url='/account/login')
@permission_required('report_OA.view_reportscontent',login_url='/account/login')
def report_list(request):
    car_id = request.GET.get('car_id')
    reports = ReportsContent.objects.all()
    if request.GET.get('input_data'):
        if request.GET.get("w_col") == 'car_brand_model':
            cars=CarAbout.objects.filter(car_brand_model__contains=request.GET.get('input_data'))
            reports=ReportsContent.objects.filter(car_id__in=cars)
        elif request.GET.get("w_col") == 'car_license_tag_number':
            cars = CarAbout.objects.filter(car_license_tag_number__contains=request.GET.get('input_data'))
            reports = ReportsContent.objects.filter(car_id__in=cars)
        elif request.GET.get("w_col") == 'car_id':
            cars = CarAbout.objects.filter(car_id__contains=request.GET.get('input_data'))
            reports = ReportsContent.objects.filter(car_id__in=cars)
        elif request.GET.get("w_col") == 'first_checker':
            users = User.objects.filter(username__contains=request.GET.get('input_data'))
            report1=ReportsContent1.objects.filter(first_checker__in=users)
            reports = ReportsContent.objects.filter(report1__in=report1)
        elif request.GET.get("w_col") == 'second_checker':
            users = User.objects.filter(username__contains=request.GET.get('input_data'))
            report1 = ReportsContent2.objects.filter(second_checker__in=users)
            reports = ReportsContent.objects.filter(report2__in=report1)
    if request.GET.get('car_id'):
        reports=ReportsContent.objects.filter(car_id=request.GET.get('car_id'))

    paginator=Paginator(reports,10)
    page = request.GET.get('page')
    try:
        current_page=paginator.page(page)
        reports =current_page.object_list
    except PageNotAnInteger:
        current_page=paginator.page(1)
        reports = current_page.object_list
    except EmptyPage:
        current_page=paginator.page(paginator.num_pages)
        reports = current_page.object_list
    return render(request, './report_list.html', {"reports": reports,"car_id":car_id})




@login_required(login_url='/account/login')
@permission_required('report_OA.view_reportscontent',login_url='/account/login')
def report_detial(request,report_id):
    report=get_object_or_404(ReportsContent,id=report_id)
    return render(request,'./report_detial.html',{"report":report})


@login_required(login_url='/account/login')
@permission_required('report_OA.change_reportscontent2',login_url='/account/login')
def report2_redit(request,report_id):
    report = ReportsContent.objects.get(id=report_id)
    car=report.car_id
    car.check_state='d_on'
    car.save()


    report2,created = ReportsContent2.objects.get_or_create(report_m=report)
    report2.second_checker=request.user
    print(request.user)
    report2.save()

    if request.method == "GET":
        report2_form = Report2ContentForm(instance=report2)
        return render(request, "./report_add.html",{"form":report2_form,"report":report})
    else:
        report2_form = Report2ContentForm(data=request.POST,instance=report2)
        if report2_form.is_valid():
            report2_form.save()
        return  redirect('/report_detial/{}'.format(report_id))

@login_required(login_url='/account/login')
@permission_required('report_OA.change_reportscontent1',login_url='/account/login')
def report1_redit(request,report_id):
    report = ReportsContent.objects.get(id=report_id)
    report1,created = ReportsContent1.objects.get_or_create(report_m=report)
    report1.first_checker=request.user
    print(request.user)
    report1.save()


    if request.method == "GET":
        report1_form = Report1ContentForm(instance=report1)
        return render(request, "./report_add.html",{"form":report1_form,"report":report})
    else:
        report1_form = Report1ContentForm(data=request.POST,instance=report1)
        if report1_form.is_valid():
            report1_form.save()
        return  redirect('/report_detial/{}'.format(report_id))


@login_required(login_url='/account/login')
@permission_required('report_OA.del_reportscontent',login_url='/account/login')
@require_POST
def report_del(request):
    report_id = request.POST['report_id']
    try:
        report = ReportsContent.objects.get(id=report_id)
        report.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("1")


# @login_required(login_url='/account/login')
# @permission_required('report_OA.add_reportscontent',login_url='/account/login')
# def report_add(request):
#     if request.method=="POST":
#         report_add_form = ReportsContentForm(data=request.POST)
#         if report_add_form.is_valid():
#             cd = report_add_form.cleaned_data
#             try:
#                 new_report= report_add_form.save()
#                 return  redirect('/report_detial/{}'.format(new_report.id))
#             except Exception as e:
#                 return HttpResponse(e)
#         else:
#             return HttpResponse("3")
#     else:
#         car_id=request.GET.get("car_id")
#         report_add_form = ReportsContentForm(initial={"car_id":car_id})
#
#         return render(request, "./report_add.html",{"form":report_add_form})


@login_required(login_url='/account/login')
@permission_required('report_OA.add_reportscontent',login_url='/account/login')
def report_add(request):
    car_id=request.GET.get("car_id")
    car=CarAbout.objects.get(id=car_id)
    car.check_state='p_on'
    car.save()
    new_report=ReportsContent.objects.create(car_id=car)

    return  redirect('/report_detial/{}'.format(new_report.id))

@login_required(login_url='/account/login')
@permission_required('report_OA.add_reportscontent',login_url='/account/login')
def report_print(request,report_id):
    report = ReportsContent.objects.get(id=report_id)
    car=report.car_id
    car.check_state = 'finish'
    car.save()

    return render(request, './report_print.html', {"report": report})
