from django.db import models


class User(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('User', 'User'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.role})"



class Department(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Location(models.Model):
 
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Category(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class SubCategory(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Asset(models.Model):
    CONDITION_CHOICES = [
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor'),
    ]
    LOCTION_CHOICES=[
        ('PALARIVATTOM','PALARIVATTOM'),
        ('VYTTILA','VYTTILA'),
    ]
    DEPARTMENT_CHOICES=[
        ('HRD','HRD'), 
        ('Administration','Administration'), 
        ('Placements','Placements'), 
        ('Operations','Operations'), 
        ('Students Success Department','Students Success Department'), 
        ('Admissions','Admissions'),
        ('Accounts & Finance','Accounts & Finance'), 
        ('Academics','Academics'),
        ('IT','IT'), 
        ('Digital Marketing','Digital Marketing'), 
        ('Students Success Department','Students Success Department'),
        ('Certificate','Certificate'),
        ('Sales','Sales'),
    ]
    CATEGORY_CHOICES=[
        ('Land(L001)','Land(L001)'), 
        ('Building(B001)','Building(B001)'), 
        ('Furniture Fixtures(FF001)','Furniture Fixtures(FF001)'), 
        ('Office Equipment(OE001)','Office Equipment(OE001)'),
        ('Computers(C001)','Computers(C001)'), 
        ('Plant Machinery(PM001','Plant Machinery(PM001'), 
        ('Vehicles(V001)','Vehicles(V001)'), 
        ('Intangibles(I001)','Intangibles(I001)'), 
    ]
    SUB_CATEGORY_CHOICES=[

        ('Freehold Land','Freehold Land'),
        ('Leasehold Land','Leasehold Land'), 
        ('Agricultural Land','Agricultural Land'), 
        ('Industrial Land','Industrial Land'), 
        ('Commercial Plot','Commercial Plot'), 
        ('Residential Plot','Residential Plot'), 
        ('Development Site / Vacant Land','Development Site / Vacant Land'), 
        ('Land with Building','Land with Building'), 
        ('Office Building','Office Building'), 
        ('Factory Building','Factory Building'), 
        ('Warehouse / Godown','Warehouse / Godown'), 
        ('Residential Building','Residential Building'), 
        ('Leasehold Improvements','Leasehold Improvements'), 
        ('Electrical Installations','Electrical Installations'), 
        ('Temporary Structure','Temporary Structure'), 
        ('Office Chair','Office Chair'), 

    ]


    category = models.ForeignKey(Category, on_delete=models.CASCADE,choices=CATEGORY_CHOICES)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE,choices=SUB_CATEGORY_CHOICES)
    asset_name = models.CharField(max_length=150)
    make_model = models.CharField(max_length=150, blank=True, null=True)
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,choices=LOCTION_CHOICES)
    assigned_to = models.CharField(max_length=100, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,choices=DEPARTMENT_CHOICES)
    purchase_date = models.DateField()
    warranty_expiry = models.DateField(blank=True, null=True)
    condition = models.CharField(max_length=10,choices=CONDITION_CHOICES)
    remarks = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.asset_name

