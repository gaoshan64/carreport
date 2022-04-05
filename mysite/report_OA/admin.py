from django.contrib import admin
from .models import ReportsContent,CarAbout,Customer,ReportsContent1,ReportsContent2
from django import forms


class CarAboutAdmin(admin.ModelAdmin):
    list_display = ('car_brand_model','car_license_tag_number','first_record_o','customer')
    list_filter = ('first_record_o','car_brand_model')
    search_fields=('car_id','car_brand_model','car_license_tag_number')
    #raw_id_fields = ("customer",)
    date_hierarchy = "first_record_o"
    ordering = ['first_record_o','car_brand_model']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('c_name','c_tel','c_wechat','first_record')
    list_filter =  ('c_name','c_tel','c_wechat','first_record')
    search_fields = ('c_name','c_tel','c_wechat','memo')
    date_hierarchy = "first_record"
    ordering = ['first_record', 'c_name']

class ReportAdmin1(admin.StackedInline):
    model = ReportsContent1
    fieldsets = [
        (None, {'fields': ['first_checker']}),
        ('发动机盖', {'fields': ['engine_cover_1','engine_cover_2','engine_cover_3','engine_cover_4','engine_cover_5','engine_cover_image']}),
        ('左前翼子板',{'fields': ['lfy_1', 'lfy_2', 'lfy_3','lfy_image']}),
        ('左前门',{'fields': ['lfd_1', 'lfd_2', 'lfd_3', 'lfd_4', 'lfd_5','lfd_image']}),
        ('左后门', {'fields': ['lrd_1', 'lrd_2', 'lrd_3', 'lrd_4', 'lrd_5', 'lrd_image']}),
        ('左后翼子板', {'fields': ['lry_1', 'lry_2', 'lry_3', 'lry_image']}),
        ('后尾门', {'fields': ['td_1', 'td_2', 'td_3', 'td_4', 'td_5', 'td_image']}),
        ('右后翼子板', {'fields': ['rry_1', 'rry_2', 'rry_3', 'rry_image']}),
        ('右后门', {'fields': ['rrd_1', 'rrd_2', 'rrd_3', 'rrd_4', 'rrd_5', 'rrd_image']}),
        ('右前门', {'fields': ['rfd_1', 'rfd_2', 'rfd_3', 'rfd_4', 'rfd_5', 'rfd_image']}),
        ('右前翼子板', {'fields': ['rfy_1', 'rfy_2', 'rfy_3', 'rfy_image']}),
        ('右侧A柱外', {'fields': ['raw_1', 'raw_2', 'raw_3', 'raw_image']}),
        ('右前门框架', {'fields': ['rfdk_1', 'rfdk_2', 'rfdk_3', 'rfdk_image']}),
        ('右前门底坎', {'fields': ['rfdd_1', 'rfdd_2', 'rfdd_3', 'rfdd_image']}),
        ('右B柱', {'fields': ['rb_1', 'rb_2', 'rb_3', 'rb_image']}),
        ('右后门框架', {'fields': ['rrdk_1', 'rrdk_2', 'rrdk_3', 'rrdk_image']}),
        ('右后门底坎', {'fields': ['rrdd_1', 'rrdd_2', 'rrdd_3', 'rrdd_image']}),
        ('右C柱', {'fields': ['rc_1', 'rc_2', 'rc_3', 'rc_image']}),
        ('左C柱', {'fields': ['lc_1', 'lc_2', 'lc_3', 'lc_image']}),
        ('左后门框架', {'fields': ['lrdk_1', 'lrdk_2', 'lrdk_3', 'lrdk_image']}),
        ('左后门底坎', {'fields': ['lrdd_1', 'lrdd_2', 'lrdd_3', 'lrdd_image']}),
        ('左B柱', {'fields': ['lb_1', 'lb_2', 'lb_3', 'lb_image']}),
        ('左前门框架', {'fields': ['lfdk_1', 'lfdk_2', 'lfdk_3', 'lfdk_image']}),
        ('左前门底坎', {'fields': ['lfdd_1', 'lfdd_2', 'lfdd_3', 'lfdd_image']}),
        ('左侧A柱外', {'fields': ['law_1', 'law_2', 'law_3', 'law_image']}),
        ('发动机仓动力部分', {'fields': ['wboxk', 'light', 'engine_desc']}),
        ('车辆底盘部分', {'fields': ['oil_leak_d', 'chassis_d']}),






    ]

class ReportAdmin2(admin.StackedInline):
    model = ReportsContent2





class ReportAdmin(admin.ModelAdmin):
    # list_display = ('car_id','car_license_tag_number','car_level','first_checker','second_checker','create_date')
    list_display = ('car_id', 'car_license_tag_number', 'car_level', 'first_checker','second_checker','create_date')
    search_fields = ('car_u_c_describe',)
    date_hierarchy = 'create_date'
    inlines = (ReportAdmin1,ReportAdmin2)


    def car_license_tag_number(self,ReportsContent):
        return ReportsContent.car_id.car_license_tag_number


    def car_level(self,ReportsContent):
       return  ReportsContent2.objects.get(report_m=ReportsContent.id).car_level


    def first_checker(self,ReportsContent):
        return ReportsContent1.objects.get(report_m=ReportsContent.id).first_checker


    def second_checker(self, ReportsContent):
        return ReportsContent2.objects.get(report_m=ReportsContent.id).second_checker







# Register your models here.
admin.site.register(ReportsContent,ReportAdmin)
admin.site.register(CarAbout,CarAboutAdmin)
admin.site.register(Customer,CustomerAdmin)
