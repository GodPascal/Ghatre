from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels

GENDER_CHOICES = [
    ('male', _('Male')),
    ('female', _('Female')),
    ('other', _('Other')),
]

NATIONALITY_CHOICES = [
    ('iranian', _('Iranian')),
    ('other', _('Other')),
]

PROVINCES_OF_IRAN_CHOICES = [
    ('alborz', _('Alborz')),
    ('ardabil', _('Ardabil')),
    ('bushehr', _('Bushehr')),
    ('chaharmahal_and_bakhtiari', _('Chaharmahal and Bakhtiari')),
    ('east_azerbaijan', _('East Azerbaijan')),
    ('isfahan', _('Isfahan')),
    ('fars', _('Fars')),
    ('gilan', _('Gilan')),
    ('golestan', _('Golestan')),
    ('hamadan', _('Hamadan')),
    ('hormozgan', _('Hormozgan')),
    ('ilam', _('Ilam')),
    ('kerman', _('Kerman')),
    ('kermanshah', _('Kermanshah')),
    ('khuzestan', _('Khuzestan')),
    ('kohgiluyeh_and_boyer_ahmad', _('Kohgiluyeh and Boyer-Ahmad')),
    ('kurdistan', _('Kurdistan')),
    ('lorestan', _('Lorestan')),
    ('markazi', _('Markazi')),
    ('mazandaran', _('Mazandaran')),
    ('north_khorasan', _('North Khorasan')),
    ('qazvin', _('Qazvin')),
    ('qom', _('Qom')),
    ('razavi_khorasan', _('Razavi Khorasan')),
    ('semnan', _('Semnan')),
    ('sistan_and_baluchestan', _('Sistan and Baluchestan')),
    ('south_khorasan', _('South Khorasan')),
    ('tehran', _('Tehran')),
    ('west_azerbaijan', _('West Azerbaijan')),
    ('yazd', _('Yazd')),
    ('zanjan', _('Zanjan')),
    ('not_iranian', _('Not Iranian'))
]

MARITAL_STATUS_CHOICES = [
    ('single', _('Single')),
    ('married', _('Married')),
    ('divorced', _('Divorced')),
    ('widowed', _('Widowed')),
]

SOCIAL_INSURANCE_TYPE_CHOICES = [
    ('health_insurance', _('Health Insurance')),
    ('social_security', _('Social Security')),
    ('unemployment_insurance', _('Unemployment Insurance')),
    ('retirement_pension', _('Retirement Pension')),
    ('none', _('None')),
]

EDUCATIONAL_STATUS_CHOICES = [
    ('elementary', 'ابتدایی'),
    ('middle_school', 'سیکل'),
    ('high_school_diploma', 'دیپلم'),
    ('associate_degree', 'فوق دیپلم'),
    ('bachelors_degree', 'کارشناسی'),
    ('masters_degree', 'کارشناسی ارشد'),
    ('doctorate', 'دکتری'),
    ('none', 'ندارد'),
]

HOUSING_STATUS_CHOICES = [
    ('owner', 'مالک'),
    ('rental', 'استیجاری- اجاره'),
    ('mortgaged', 'استیجاری - رهن'),
    ('mortgaged_rental', 'استیجاری - رهن و اجاره'),
    ('endowment', 'اوقاف'),
    ('relatives', 'بستگان'),
]

DOCUMENT_TYPE_CHOICES = [
    ('birth_certificate','شناسنامه'),
    ('id_card','کارت ملی'),
    ('guardian_id_card','کارت ملی سرپرست خانوار'),
    ('guardian_birth_certificate','شناسنامه سرپرست خانوار'),
    ('job_certificate','مدرک شغلی'),
    ('property_certificate','مدرک ملکی'),
    ('drugs_images','تصویر داروها'),
    ('supplementary_insurance','بیمه تکمیلی'),
    ('insurance_letter','معرفی‌نامه بیمه'),    
    ('introduction_letter','معرفی‌نامه'),
    ('prescription','نسخه'),
    ('pre_invoice','پیش فاکتور'),
    ('case_sheet','برگه خلاصه پرونده'),
    ('doctor_note','گواهی پزشک'),
    ('lab_results','نتایج آزمایش‌ها'),
    ('radiology','عکس‌برداری'),
    ('statement','فرم اظهارنامه'),
    ('special_medicine_form','فرم داروهای تک‌نسخه‌ای'),
    
]

DISEASE_TYPE_CHOICES = [
    ('Infectious and parasitic','عفونی و انگلی'),
    ('Cancer and blood diseases','سرطان و بیماری های خونی'),
    ('Safety system','سیستم ایمنی'),
    ('Glands','غدد'),
    ('Psychiatry','اعصاب و روان'),
    ('Neurology','مغز و اعصاب'),
    ('Eye disease','بیماری چشمی'),
    ('Ear nose and throat','گوش و حلق و بینی'),
    ('Cardiovascular','قلبی-عروقی'),
    ('Respiratory','تنفسی'),
    ('Digestive','گوارشی'),
    ('Skin','پوستی'),
    ('Musculoskeletal','عضلانی-اسکلتی'),
    ('Kidney and genitourinary tract','کلیه و مجاری ادراری-تناسلی'),
    ('Obstetrics and Gynecology','زنان و زایمان '),
    ('Genetic and congenital','ژنتیکی و مادرزادی '),
    ('Accidents','سوانح'),
    ('other','سایر'),

]


class PatientCase(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Creator'))

    active = models.BooleanField(default=True, verbose_name=_('Active'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))
    first_name = models.CharField(max_length=255, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=255, verbose_name=_('Last Name'))
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name=_('Gender'))
    birthdate = models.DateField(verbose_name=_('Birthdate'))
    national_code = models.CharField(max_length=10, verbose_name=_('National Code'))
    nationality = models.CharField(max_length=10, choices=NATIONALITY_CHOICES, verbose_name=_('Nationality'))

    first_guardian_name = models.CharField(max_length=255, verbose_name=_('First Guardian Name'))
    first_guardian_national_code = models.CharField(max_length=10, blank=True, verbose_name=_('First Guardian National Code'))
    first_guardian_relation = models.CharField(max_length=255, verbose_name=_('First Guardian Relation'))
    second_guardian_name = models.CharField(max_length=255, blank=True, verbose_name=_('Second Guardian Name'))
    second_guardian_national_code = models.CharField(max_length=10, blank=True, verbose_name=_('Second Guardian National Code'))
    second_guardian_relation = models.CharField(max_length=255, blank=True, verbose_name=_('Second Guardian Relation'))

    social_insurance_type = models.CharField(max_length=255, choices=SOCIAL_INSURANCE_TYPE_CHOICES, verbose_name=_('Social Insurance Type'))
    social_insurance_number = models.CharField(max_length=255, blank=True, verbose_name=_('Social Insurance Number'))
    social_insurance_description = models.TextField(blank=True, verbose_name=_('Social Insurance Description'))

    educational_status = models.CharField(max_length=20, choices=EDUCATIONAL_STATUS_CHOICES, verbose_name=_('Educational Status'))

    has_private_insurance = models.BooleanField(verbose_name=_('Has Private Insurance'))
    private_insurance_name = models.TextField(blank=True, verbose_name=_('Private Insurance Name'))
    private_insurance_number = models.CharField(max_length=255, blank=True, verbose_name=_('Private Insurance Number'))

    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, verbose_name=_('Marital Status'))
    marital_status_description = models.TextField(blank=True, verbose_name=_('Marital Status Description'))

    housing_status = models.CharField(max_length=20, choices=HOUSING_STATUS_CHOICES, verbose_name=_('Housing Status'))
    deposit_amount = models.IntegerField(blank=True, null=True, verbose_name=_('Deposit Amount'))
    rent_amount = models.IntegerField(blank=True, null=True, verbose_name=_('Rent Amount'))

    has_job = models.BooleanField(null=True, verbose_name=_('Has Job'))
    monthly_income = models.IntegerField(verbose_name=_('Monthly Income'))
    subsidy = models.IntegerField(verbose_name=_('Subsidy'))
    family_monthly_expenses = models.IntegerField(verbose_name=_('Family Monthly Expenses'))
    amount_of_installment_or_debt = models.IntegerField(verbose_name=_('Amount of Installment or Debt'))
    repayment_due_date = models.DateField(verbose_name=_('Repayment Due Date'))
    income_expenses_description = models.TextField(blank=True, verbose_name=_('Income Expenses Description'))
    
    province_of_residence = models.CharField(max_length=30, choices=PROVINCES_OF_IRAN_CHOICES, blank=True, verbose_name=_('Province of Residence'))
    city_of_residence = models.CharField(max_length=255, blank=True, verbose_name=_('City of Residence'))
    address = models.TextField(blank=True, verbose_name=_('Address'))
     
    mobile_number = models.CharField(max_length=20, verbose_name=_('Mobile Number'))
    phone_number = models.CharField(max_length=20, blank=True, verbose_name=_('Phone Number'))
    
    representor = models.CharField(max_length=255, verbose_name=_('Representor'))
    representor_relation = models.CharField(max_length=255, verbose_name=_('Representor Relation'))
    
    referrer_name = models.CharField(max_length=255, verbose_name=_('Referrer Name'))

    other_information = models.TextField(blank=True, verbose_name=_('Other Information'))

    patient_problem = models.TextField(blank=True, verbose_name=_('Patient Problem'))
    helper_comment = models.TextField(blank=True, verbose_name=_('Helper Comment'))

    class Meta:
        verbose_name = _('Patient Case')
        verbose_name_plural = _('Patient Cases')
    
    def __str__(self) -> str:
        return '%s       %s' % (self.first_name, self.last_name)


class Relative(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))

    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))
    first_name = models.CharField(max_length=255, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=255, verbose_name=_('Last Name'))
    relation = models.CharField(max_length=255, verbose_name=_('Relation'))
    year_of_birth = models.IntegerField(verbose_name=_('Year of Birth'))
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, verbose_name=_('Marital Status'))
    occupation = models.CharField(max_length=255, verbose_name=_('Occupation'))
    monthly_income = models.IntegerField(verbose_name=_('Monthly Income'))
    health_status = models.CharField(max_length=255, verbose_name=_('Health Status'))

    class Meta:
        verbose_name = _('Relative')
        verbose_name_plural = _('Relatives')


class OtherSupporter(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))

    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    support_amount = models.IntegerField(verbose_name=_('Support Amount'))
    support_start = models.DateField(verbose_name=_('Support Start'))
    support_end = models.DateField(verbose_name=_('Support End'))
    other_information = models.TextField(blank=True, verbose_name=_('Other Information'))

    class Meta:
        verbose_name = _('Other Supporter')
        verbose_name_plural = _('Other Supporters')

class Document(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))
    type = models.CharField(max_length=30, choices=DOCUMENT_TYPE_CHOICES, verbose_name=_('Type'))
    uploaded_file = models.FileField(upload_to='documents/', verbose_name=_('File'))

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')

class MedicalRecord(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Creator'))
    disease_type = models.CharField(max_length=30, choices=DISEASE_TYPE_CHOICES, verbose_name=_('Disease Type'))
    disease_name = models.CharField(max_length=255, verbose_name=_('Disease Name'))
    second_disease_name = models.CharField(blank=True, max_length=255, verbose_name=_('Disease Name (2nd)'))
    diagnosis_year = models.IntegerField(verbose_name=_('Diagnosis Year'))

    diagnosis = models.TextField(blank=True, verbose_name=_('Diagnosis'))
    diagnosis_tests = models.TextField(blank=True, verbose_name=_('Diagnosis Tests'))
    drug_history = models.TextField(blank=True, verbose_name=_('Drug History'))
    surgery_history = models.TextField(blank=True, verbose_name=_('Surgery History'))
    other_diseases = models.TextField(blank=True, verbose_name=_('Other Diseases'))
    dietary_habits = models.TextField(blank=True, verbose_name=_('Dietary Habits'))
    movement_ability = models.CharField(blank=True, max_length=255, verbose_name=_('Movement Ability'))
    routines_ability = models.CharField(blank=True, max_length=255, verbose_name=_('Routines Ability'))
    talking_and_swallowing = models.CharField(blank=True, max_length=255, verbose_name=_('Talking and Swallowing'))
    gatherings_attending = models.CharField(blank=True, max_length=255, verbose_name=_('Gatherings Attending'))
    family_and_social = models.CharField(blank=True, max_length=255, verbose_name=_('ّFamily and Social'))
    
    height = models.FloatField(null=True, blank=True, verbose_name=_('Height'))
    weight = models.FloatField(null=True, blank=True, verbose_name=_('Weight'))

    drugs_abuse = models.CharField(blank=True, max_length=255, verbose_name=_('Drugs Abuse'))
    other_information = models.CharField(blank=True, max_length=255, verbose_name=_('Other Information'))
    treatment_facilities = models.CharField(blank=True, max_length=255, verbose_name=_('Treatment Facilities'))
    doctors_names = models.CharField(blank=True, max_length=255, verbose_name=_('Doctors Names'))

    class Meta:
        verbose_name = _('Medical Record')
        verbose_name_plural = _('Medical Records')     

class GenericDrug(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Generic Drug')
        verbose_name_plural = _('Generic Drugs')

class DrugBrand(models.Model):
    brand_name = models.CharField(max_length=255, verbose_name=_('Brand Name'))
    country = models.CharField(max_length=30, verbose_name=_('Country'))
    address = models.CharField(max_length=255, verbose_name=_('Address'))
    phone = models.CharField(max_length=20, verbose_name=_('Phone'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = _('Drug Brand')
        verbose_name_plural = _('Drug Brands')

class PatientDrug(models.Model):
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))
    
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    generic_drug = models.ForeignKey(GenericDrug, on_delete=models.CASCADE, verbose_name=_('Generic Drug'))
    drug_brand = models.ForeignKey(DrugBrand, on_delete=models.CASCADE, verbose_name=_('Drug Brand'))
    
    usage_start = models.CharField(max_length=30, verbose_name=_('Usage Start'))
    usage_duration = models.CharField(max_length=30, verbose_name=_('Usage Duration'))
    usage_instruction = models.CharField(max_length=30, verbose_name=_('Usage Instruction'))
    costs = models.IntegerField(null=True, blank=True, verbose_name=_('Costs'))

    class Meta:
        verbose_name = _('Patient Drug')
        verbose_name_plural = _('Patient Drugs')