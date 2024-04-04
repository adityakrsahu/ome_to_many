from django.db import models

# Create your models here.
depaetments=[('ECE','ECE'),
             ('CSE','CSE'),
             ('EXE','EXE'),
             ('IT','IT'),
             ('ME','ME'),
             ('MI/ML','MI/ML')
            ]
class DepartmentModel(models.Model):
    dep_name = models.CharField(max_length=100,verbose_name='Name',choices=depaetments)
    description = models.TextField(max_length=200,verbose_name='Desc')
    def __str__(self):
        return self.dep_name
cources = [
    ('1','B.tech'),
    ('2','M.tech'),
    ('3','B.Com'),
    ('4','M.Com'),
    ('5','BCA'),
    ('6','MCA'),
]

class StudentModel(models.Model):
    stu_name=models.CharField(max_length=100,verbose_name='Name')
    stu_class=models.CharField(max_length=100,verbose_name='Class',choices=cources)
    stu_email=models.EmailField()
    stu_mobile=models.IntegerField()
    # stu_department=models.ForeignKey(DepartmentModel,on_delete=models.CASCADE,null=True)
    stu_department=models.ForeignKey(DepartmentModel,on_delete=models.PROTECT,null=True)
    def __str__(self):
        return self.stu_name