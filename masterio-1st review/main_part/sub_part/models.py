from django.db import models

# Create your models here.
class reg1(models.Model):
    name=models.CharField(max_length=100)
    mail_id=models.EmailField()
    phone_number=models.CharField(max_length=15)
    
    
    def __str__(self):
        return self.name
class reg2(models.Model):
    Username=models.CharField(max_length=100)
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Mail_id=models.EmailField()
    password=models.CharField(max_length=100)
    

    def __str__(self):
        return self.Username
class reg3(models.Model):
    Username=models.CharField(max_length=100)
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Mail_id=models.EmailField()
    password=models.CharField(max_length=100)
    

    def __str__(self):
        return self.Username

class reg4(models.Model):
    Username=models.CharField(max_length=100)
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Mail_id=models.EmailField()
    password=models.CharField(max_length=100)
    

    def __str__(self):
        return self.Username
class reg5(models.Model):
    name=models.CharField(max_length=100)
    E_Mail=models.EmailField()
    Password=models.CharField(max_length=100)
    Confirm_Password=models.CharField(max_length=100)

    def __str__(self):
        return self.name
class reg6(models.Model):
    Name=models.CharField(max_length=100)
    E_Mail=models.EmailField()
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.Name
class cont(models.Model):
    your_name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)
    messege=models.TextField()

    def __str__(self):
        return self.your_name
class reg8(models.Model):
    Password=models.CharField(max_length=100)
    token=models.CharField(max_length=100)

    def __str__(self):
        return self.Password 

class reg9(models.Model):
    Enter_course_title=models.CharField(max_length=100)
    from_url=models.CharField(max_length=100)
    fileToUpload=models.ImageField()
    overview_URL=models.CharField(max_length=100)
    Enter_requirements=models.CharField(max_length=100)
    Enter_outcome=models.CharField(max_length=100)
    Enter_tags=models.CharField(max_length=100)
    Amount=models.CharField(max_length=100)
    Enter_meta_title=models.CharField(max_length=100)
    Short_description=models.TextField()
    Meta_description=models.TextField()
    Course_level=models.CharField(max_length=100)
    Provider=models.CharField(max_length=100)
    Free_course=models.CharField(max_length=100)
    Discount=models.CharField(max_length=100)
    Language=models.CharField(max_length=100)
    Category=models.CharField(max_length=100)
    def __str__(self):
        return self.Enter_course_title 


class drop(models.Model):
    Enter_Price=models.CharField(max_length=100)
    Commission=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/%Y/%m/%d',null=True,blank=True)

    def __str__(self):
        return self.Enter_Price
class category(models.Model):
    Enter_Price=models.CharField(max_length=100)
    Parent_Category=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/%Y/%m/%d',null=True,blank=True)

    def __str__(self):
        return self.Enter_Price