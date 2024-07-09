from django.utils.translation import gettext_lazy as _

GENDER_CHOICES = [
  ('male', _('Male')),
  ('female', _('Female')),
  ('other', _('Other')),
]

NATIONALITY_CHOICES = [
  ('iranian', _('Iranian')),
  ('other', _('Other')),
]

GUARDIAN_STATUS_CHOICES = [
  ('self', _('Self')),
  ('other', _('Other'))
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
  ('temp_married', _('Temp Married')),
  ('divorced', _('Divorced')),
  ('widowed', _('Widowed')),
  ('separated', _('Separated'))
]

SOCIAL_INSURANCE_TYPE_CHOICES = [
  ('health_insurance', _('Health Insurance')),
  ('social_security', _('Social Security')),
  ('medical_services', _('Medical Services')),
  ('armed_forces', _('Armed Forces')),
  ('other', _('Other')),
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
  ('janitor', 'سرایدار'),
  ('other', _('Other'))
]

DOCUMENT_TYPE_CHOICES = [
  ('birth_certificate', 'شناسنامه'),
  ('id_card', 'کارت ملی'),
  ('guardian_id_card', 'کارت ملی سرپرست خانوار'),
  ('guardian_birth_certificate', 'شناسنامه سرپرست خانوار'),
  ('job_certificate', 'مدرک شغلی'),
  ('property_certificate', 'مدرک ملکی'),
  ('drugs_images', 'تصویر داروها'),
  ('supplementary_insurance', 'بیمه تکمیلی'),
  ('insurance_letter', 'معرفی‌نامه بیمه'),
  ('introduction_letter', 'معرفی‌نامه'),
  ('prescription', 'نسخه'),
  ('pre_invoice', 'پیش فاکتور'),
  ('case_sheet', 'برگه خلاصه پرونده'),
  ('doctor_note', 'گواهی پزشک'),
  ('lab_results', 'نتایج آزمایش‌ها'),
  ('radiology', 'عکس‌برداری'),
  ('statement', 'فرم اظهارنامه'),
  ('special_medicine_form', 'فرم داروهای تک‌نسخه‌ای'),

]
DISEASE_TYPE_CHOICES = [
  ('infectious_and_parasitic', 'عفونی و انگلی'),
  ('cancer_and_blood_diseases', 'سرطان و بیماری های خونی'),
  ('safety_system', 'سیستم ایمنی'),
  ('glands', 'غدد'),
  ('psychiatry', 'اعصاب و روان'),
  ('neurology', 'مغز و اعصاب'),
  ('eye_disease', 'بیماری چشمی'),
  ('ear_nose_throat', 'گوش و حلق و بینی'),
  ('cardiovascular', 'قلبی-عروقی'),
  ('respiratory', 'تنفسی'),
  ('digestive', 'گوارشی'),
  ('skin', 'پوستی'),
  ('susculoskeletal', 'عضلانی-اسکلتی'),
  ('kidney_genitourinary_tract', 'کلیه و مجاری ادراری-تناسلی'),
  ('gynecology', 'زنان و زایمان '),
  ('genetic', 'ژنتیکی و مادرزادی '),
  ('accidents', 'سوانح'),
  ('other', 'سایر'),

]

DISEASE_STATUS_CHOICES = [
  ('in_progress', _('Treatment In Progress')),
  ('stopped', _('Treatment Stopped')),
  ('cured', _('Cured')),
]

PATIENT_DOCTOR_STATUS_CHOICES = [
  ('active', _('Active')),
  ('inactive', _('Inactive'))
]

PATIENT_DRUG_LIST_STATUS_CHOICES = [
  ('single_prescription', _('Single Prescription')),
  ('without_insurance', _('Without Insurance')),
  ('other', _('Other'))
]

PATIENT_DRUG_STATUS_CHOICES = [
  ('active', _('Active')),
  ('inactive', _('Inactive'))
]

DRAFT_TYPE_CHOICES = [
  ('P', 'P'),
  ('IT', 'IT')
]

DRAFT_STATUS_CHOICES = [
  ('active', 'فعال'),
  ('inactive', 'غیرفعال'),
  ('pending', 'در انتظار'),
]

SUPPLIER_TYPE_CHOICES = [
  ('pharmacy', 'داروخانه'),
  ('factory', 'کارخانه')
]

INPUT_LOG_STATUS_CHOICES = [
  ('reception', _('Reception')),
  ('waiting', _('Waiting'))
]

PATIENT_CASE_STATUS_CHOICES = [
    ('active', _('Active')),
    ('inactive', _('Inactive')),
    ('waiting', _('Waiting')),
    ('semi-active', _('Semi Active'))
]

DESCRIPTION_OF_THE_LAST_ACTION = [
    ('interview_appointment_set', 'تنظیم قرار مصاحبه'),
    ('file_created', 'تشکیل پرونده'),
    ('under_review', 'در حال بررسی'),
    ('referred', 'ارجاع'),
    ('waiting_foreign_single_dose', 'در انتظار- تک نسخه ای خارجی'),
    ('waiting_domestic_single_dose', 'در انتظار- تک نسخه ای داخلی'),
    ('waiting_expensive', 'در انتظار- گران قیمت'),
    ('waiting_foreign_nationals', 'در انتظار - اتباع'),
    ('no_response', 'عدم پاسخگویی'),
    ('patient_did_not_create_file', 'عدم مراجعه بیمار برای تشکیل پرونده'),
    ('resident_of_city', 'ساکن شهرستان'),
    ('covered_by_other_charities', 'پوشش سایر خیریه ها'),
    ('covered_by_basic_insurance', 'پوشش بیمه پایه'),
    ('covered_by_supplementary_insurance', 'پوشش بیمه تکمیلی'),
    ('no_drug_needed', 'عدم نیاز دارویی'),
    ('financial_aid_requested', 'درخواست کمک مالی'),
    ('treatment_completed', 'اتمام دوره درمان'),
    ('patient_unwilling_to_follow_up', 'عدم تمایل و پیگیری بیمار'),
    ('drug_equipment_requested', 'درخواست تجهیزات دارویی'),
    ('drug_regimen_changed', 'تغییر رژیم دارویی'),
    ('no_contract_pharmacy', 'عدم داروخانه طرف قرارداد'),
    ('deceased', 'فوت'),
    ('other', 'سایر')]
INPUT_DRAFT_STATUS_CHOICES = [
    ('identified', 'شناسایی شده'),
    ('evaluated', 'ارزیابی شده'),
    ('accepted', 'پذیرش'),
    ('rejected', 'عدم پذیرش'),
    ('waiting', 'در انتظار')
]
