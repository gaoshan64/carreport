from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ajaximage.fields import AjaxImageField
from django.db.models import BooleanField as _BooleanField


# Create your models here.
class ReportsContent(models.Model):
    car_id = models.ForeignKey(verbose_name='车辆信息', to='CarAbout', on_delete=models.CASCADE, related_name='car_report')
    create_date = models.DateTimeField(auto_now_add=True, auto_created=True)

    class Meta:
        ordering = ("-create_date",)

    def __str__(self):
        return str(self.car_id) + str(self.create_date)





class ReportsContent1(models.Model):
    first_checker = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="first_check_report", null=True,
                                      verbose_name='初检人')
    report_m = models.OneToOneField(ReportsContent, on_delete=models.CASCADE, null=True, related_name='report1')
    #发动机盖
    engine_cover_1=models.IntegerField('左上',default=0)
    engine_cover_2 = models.IntegerField('左下', default=0)
    engine_cover_3 = models.IntegerField('中', default=0)
    engine_cover_4 = models.IntegerField('右上', default=0)
    engine_cover_5 = models.IntegerField('右下', default=0)
    engine_cover_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    #左前翼子板
    lfy_1 = models.IntegerField('前', default=0)
    lfy_2 = models.IntegerField('中', default=0)
    lfy_3 = models.IntegerField('后', default=0)
    lfy_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    #左前门
    lfd_1 = models.IntegerField('左上', default=0)
    lfd_2 = models.IntegerField('左下', default=0)
    lfd_3 = models.IntegerField('中', default=0)
    lfd_4 = models.IntegerField('右上', default=0)
    lfd_5 = models.IntegerField('右下', default=0)
    lfd_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    #左后门
    lrd_1 = models.IntegerField('左上', default=0)
    lrd_2 = models.IntegerField('左下', default=0)
    lrd_3 = models.IntegerField('中', default=0)
    lrd_4 = models.IntegerField('右上', default=0)
    lrd_5 = models.IntegerField('右下', default=0)
    lrd_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    #左后翼子板
    lry_1 = models.IntegerField('前', default=0)
    lry_2 = models.IntegerField('中', default=0)
    lry_3 = models.IntegerField('后', default=0)
    lry_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    #后尾门
    td_1 = models.IntegerField('左上', default=0)
    td_2 = models.IntegerField('左下', default=0)
    td_3 = models.IntegerField('中', default=0)
    td_4 = models.IntegerField('右上', default=0)
    td_5 = models.IntegerField('右下', default=0)
    td_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    # 右后翼子板
    rry_1 = models.IntegerField('前', default=0)
    rry_2 = models.IntegerField('中', default=0)
    rry_3 = models.IntegerField('后', default=0)
    rry_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    # 右后门
    rrd_1 = models.IntegerField('左上', default=0)
    rrd_2 = models.IntegerField('左下', default=0)
    rrd_3 = models.IntegerField('中', default=0)
    rrd_4 = models.IntegerField('右上', default=0)
    rrd_5 = models.IntegerField('右下', default=0)
    rrd_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    # 右前门
    rfd_1 = models.IntegerField('左上', default=0)
    rfd_2 = models.IntegerField('左下', default=0)
    rfd_3 = models.IntegerField('中', default=0)
    rfd_4 = models.IntegerField('右上', default=0)
    rfd_5 = models.IntegerField('右下', default=0)
    rfd_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    # 右前翼子板
    rfy_1 = models.IntegerField('前', default=0)
    rfy_2 = models.IntegerField('中', default=0)
    rfy_3 = models.IntegerField('后', default=0)
    rfy_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    #右侧A柱外
    raw_1 = models.IntegerField('上', default=0)
    raw_2 = models.IntegerField('中', default=0)
    raw_3 = models.IntegerField('下', default=0)
    raw_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    #右前门框架
    rfdk_1 = models.IntegerField('前', default=0)
    rfdk_2 = models.IntegerField('中', default=0)
    rfdk_3 = models.IntegerField('后', default=0)
    rfdk_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    #右前门底坎
    rfdd_1 = models.IntegerField('前', default=0)
    rfdd_2 = models.IntegerField('中', default=0)
    rfdd_3 = models.IntegerField('后', default=0)
    rfdd_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    #右B柱
    rb_1 = models.IntegerField('上', default=0)
    rb_2 = models.IntegerField('中', default=0)
    rb_3 = models.IntegerField('下', default=0)
    rb_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    # 右后门框架
    rrdk_1 = models.IntegerField('前', default=0)
    rrdk_2 = models.IntegerField('中', default=0)
    rrdk_3 = models.IntegerField('后', default=0)
    rrdk_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    # 右后门底坎
    rrdd_1 = models.IntegerField('前', default=0)
    rrdd_2 = models.IntegerField('中', default=0)
    rrdd_3 = models.IntegerField('后', default=0)
    rrdd_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    #右C柱
    rc_1 = models.IntegerField('上', default=0)
    rc_2 = models.IntegerField('中', default=0)
    rc_3 = models.IntegerField('下', default=0)
    rc_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    #左C柱
    lc_1 = models.IntegerField('上', default=0)
    lc_2 = models.IntegerField('中', default=0)
    lc_3 = models.IntegerField('下', default=0)
    lc_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    # 左后门框架
    lrdk_1 = models.IntegerField('前', default=0)
    lrdk_2 = models.IntegerField('中', default=0)
    lrdk_3 = models.IntegerField('后', default=0)
    lrdk_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    # 左后门底坎
    lrdd_1 = models.IntegerField('前', default=0)
    lrdd_2 = models.IntegerField('中', default=0)
    lrdd_3 = models.IntegerField('后', default=0)
    lrdd_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    #左B柱
    lb_1 = models.IntegerField('上', default=0)
    lb_2 = models.IntegerField('中', default=0)
    lb_3 = models.IntegerField('下', default=0)
    lb_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    # 左前门框架
    lfdk_1 = models.IntegerField('前', default=0)
    lfdk_2 = models.IntegerField('中', default=0)
    lfdk_3 = models.IntegerField('后', default=0)
    lfdk_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    # 左前门底坎
    lfdd_1 = models.IntegerField('前', default=0)
    lfdd_2 = models.IntegerField('中', default=0)
    lfdd_3 = models.IntegerField('后', default=0)
    lfdd_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    #左A柱
    law_1 = models.IntegerField('上', default=0)
    law_2 = models.IntegerField('中', default=0)
    law_3 = models.IntegerField('下', default=0)
    law_image = AjaxImageField('取所有检测点中数值大的拍照上传', blank=True, max_height=600, max_width=800, crop=True)
    ## 发动机仓动力部分
    #水箱框架
    wboxk_c = (('ok', '正常'), ('na', '异常'))
    wboxk = models.CharField('水箱框架',max_length=10,choices=wboxk_c,default='ok')
    light = models.CharField('前大灯总成', max_length=10, choices=wboxk_c,default='2')
    engine_desc=models.TextField('机舱整体描述',blank=True,max_length=1000)
    ## 车辆底盘部分
    oil_leak_d=models.TextField('油液渗漏描述',blank=True,max_length=1000)
    chassis_d = models.TextField('底盘整理描述',blank=True,max_length=1000)

    def max_engine_cover(self):
        engine_list=[self.engine_cover_1,self.engine_cover_2,self.engine_cover_3,
                     self.engine_cover_4,self.engine_cover_5]
        return max(engine_list)

    def max_lfy(self):
        lfy_list=[self.lfy_1,self.lfy_2,self.lfy_3,]
        return max(lfy_list)

    def max_lfd(self):
        lfd_list=[self.lfd_1,self.lfd_2,self.lfd_3,self.lfd_4,self.lfd_5]
        return max(lfd_list)

    def max_lrd(self):
        lrd_list = [self.lrd_1, self.lrd_2, self.lrd_3, self.lrd_4, self.lrd_5]
        return max(lrd_list)

    def max_lry(self):
        lry_list=[self.lry_1,self.lry_2,self.lry_3,]
        return max(lry_list)

    def max_td(self):
        td_list = [self.td_1, self.td_2, self.td_3, self.td_4, self.td_5]
        return max(td_list)

    def max_rry(self):
        rry_list = [self.rry_1, self.rry_2, self.rry_3, ]
        return max(rry_list)

    def max_rrd(self):
        rrd_list = [self.rrd_1, self.rrd_2, self.rrd_3, self.rrd_4, self.rrd_5]
        return max(rrd_list)

    def max_rfd(self):
        rfd_list = [self.rfd_1, self.rfd_2, self.rfd_3, self.rfd_4, self.rfd_5]
        return max(rfd_list)

    def max_rfy(self):
        rfy_list = [self.rfy_1, self.rfy_2, self.rfy_3, ]
        return max(rfy_list)

    def max_raw(self):
        raw_list = [self.raw_1, self.raw_2, self.raw_3, ]
        return max(raw_list)

    def max_rfdk(self):
        rfdk_list = [self.rfdk_1, self.rfdk_2, self.rfdk_3, ]
        return max(rfdk_list)

    def max_rfdd(self):
        rfdd_list = [self.rfdd_1, self.rfdd_2, self.rfdd_3, ]
        return max(rfdd_list)

    def max_rb(self):
        rb_list = [self.rb_1, self.rb_2, self.rb_3, ]
        return max(rb_list)

    def max_rrdk(self):
        rrdk_list = [self.rrdk_1, self.rrdk_2, self.rrdk_3, ]
        return max(rrdk_list)


    def max_rrdd(self):
        rrdd_list = [self.rrdd_1, self.rrdd_2, self.rrdd_3, ]
        return max(rrdd_list)

    def max_rc(self):
        rrdd_list = [self.rc_1, self.rc_2, self.rc_3, ]
        return max(rrdd_list)

    def max_lc(self):
        rrdd_list = [self.lc_1, self.lc_2, self.lc_3, ]
        return max(rrdd_list)

    def max_lrdk(self):
        rrdd_list = [self.lrdk_1, self.lrdk_2, self.lrdk_3, ]
        return max(rrdd_list)

    def max_lrdd(self):
        lrdd_list = [self.lrdd_1, self.lrdd_2, self.lrdd_3, ]
        return max(lrdd_list)

    def max_lb(self):
        lrdd_list = [self.lb_1, self.lb_2, self.lb_3, ]
        return max(lrdd_list)

    def max_lfdk(self):
        lrdd_list = [self.lfdk_1, self.lfdk_2, self.lfdk_3, ]
        return max(lrdd_list)

    def max_lfdk(self):
        lrdd_list = [self.lfdk_1, self.lfdk_2, self.lfdk_3, ]
        return max(lrdd_list)


    def __str__(self):
        return str(self.report_m)+'初检'




class ReportsContent2(models.Model):
    id = models.BigAutoField(primary_key=True)
    #choice
    car_level_c=(('A','A'),('B','B'),('C','C'),('D','D'),('E','E'),('F','F'),('G','G'),('H','H'))
    report_m = models.OneToOneField(ReportsContent, on_delete=models.CASCADE, null=True,related_name='report2')
    second_checker = models.ForeignKey(User,on_delete=models.SET_NULL,related_name="second_check_report",null=True,verbose_name='复检人')
    #车辆检测结果
    accident_car=models.BooleanField('事故车',default=0)
    water_car = models.BooleanField('水泡车',default=0)
    fire_car=models.BooleanField('火烧车',default=0)
    #gear_box=models.CharField(max_length=10,choices=gear_box_c)
    car_level=models.CharField('车辆等级',max_length=10,choices=car_level_c,default='A')

    car_body_score=models.IntegerField('车身检查',default=0)
    car_chassis_score=models.IntegerField('底盘检查',default=0)
    car_power_score=models.IntegerField('动力检查',default=0)
    car_com_score=models.IntegerField('综合检查',default=0)
    car_score = models.IntegerField('车况得分',default=0)
    car_u_c_describe=models.TextField('异常状况描述',max_length=1000,default='')
    #
    car_b_image_zq=AjaxImageField('左前45',blank=True,max_height=600,max_width=800,crop=True)
    car_b_image_yh = AjaxImageField('右后45', blank=True,max_height=600,max_width=800,crop=True)
    car_b_image_zqzy = AjaxImageField('左前座椅', blank=True,max_height=600,max_width=800,crop=True)
    car_b_image_yhzy = AjaxImageField('右后座椅', blank=True,max_height=600,max_width=800,crop=True)

    car_b_engcab = AjaxImageField('发动机仓', blank=True, max_height=600, max_width=800, crop=True)
    car_b_rcab = AjaxImageField('后备箱', blank=True, max_height=600, max_width=800, crop=True)
    car_b_dashboard = AjaxImageField('仪表盘', blank=True, max_height=600, max_width=800, crop=True)
    car_b_ccontrol = AjaxImageField('中控台', blank=True, max_height=600, max_width=800, crop=True)

    car_b_np = AjaxImageField('车辆名牌', blank=True, max_height=600, max_width=800, crop=True)
    car_b_dm = AjaxImageField('车辆代码', blank=True, max_height=600, max_width=800, crop=True)

    def __str__(self):
        return str(self.report_m)+'复检'


class CarAbout(models.Model):

    #choice
    if_impoirt_c=(('import','进口'),('n_import','国产'))
    gear_box_c=(('m','手动'),('a','自动'))
    if_business_c=(('b','营运'),('nb','非营运'))
    fuel_type_c=(('d','柴油'),('g','汽油'),('na','NA'))
    check_state_c = (('wait','待检测'),('p_on','检测中'),('d_on','复检中'),('finish','已完成'))
    #
    customer = models.ForeignKey(verbose_name="用户", to='Customer', on_delete=models.CASCADE, related_name="customer_car", )
    car_brand_model = models.CharField("品牌型号",max_length=30)
    if_import = models.CharField("是否进口",max_length=10,choices=if_impoirt_c)
    car_license_tag_number = models.CharField('车辆牌照',max_length=20,db_index=True)
    car_id=models.CharField('车架号',max_length=30,db_index=True,unique=True,)
    car_type= models.CharField('车型',max_length=10)
    car_color = models.CharField('颜色',max_length=10,)

    licence_first=models.DateField(verbose_name="初次登记日期")
    licence_issued=models.DateField(verbose_name="上牌日期")

    first_record_o=models.DateTimeField(auto_now=True,auto_created=True)

    engine_number = models.CharField('发动机号',max_length=20)
    engine_cc = models.CharField('排量',max_length=10)
    engine_power = models.CharField('马力',max_length=10)

    engine_power_mode = models.CharField('动力方式',max_length=10)
    fuel_type = models.CharField('燃料类别',max_length=10, choices=fuel_type_c)
    drive_mode = models.CharField('驱动方式',max_length=10)

    gear_box = models.CharField('变速箱',max_length=10, choices=gear_box_c)
    manage_city = models.CharField('车辆管理属地',max_length=10)
    if_business = models.CharField('车辆使用性质',max_length=10, choices=if_business_c)
    check_state =models.CharField('车辆检测状态',max_length=10,choices=check_state_c,default='wait')
    class Meta:
        ordering = ("-first_record_o",)

    def __str__(self):
        return self.car_color+self.car_brand_model+self.car_license_tag_number


class Customer(models.Model):
    c_name=models.CharField('姓名',max_length=20,db_index=True)
    c_tel=models.CharField('电话',max_length=15,db_index=True)
    c_wechat=models.CharField('身份证',max_length=30,db_index=True,unique=True,)
    memo = models.TextField('备注',blank=True,max_length=1000)
    first_record = models.DateTimeField(auto_now_add=True, auto_created=True)

    class Meta:
        ordering = ("-first_record",)

    def __str__(self):
        return self.c_name + self.c_tel

