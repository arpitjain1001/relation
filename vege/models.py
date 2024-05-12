from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# RECEIPE MODEL
class Receipe(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL ,null = True, blank=True)
  receipe_name = models.CharField(max_length=100)
  receipe_desc = models.TextField()
  receipe_image= models.ImageField(upload_to="images")
  

# DEPARTMENT MODEL
class Department(models.Model):
    department = models.CharField(max_length=100)
    def __str__(self):
       return self.department
    class Meta:
        ordering = ['department']


# STUDENTID MODEL
class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self):
       return self.student_id
                                

# STUDENT MODEL
class Student(models.Model):
     department = models.ForeignKey(Department , related_name="depart" ,on_delete=models.CASCADE)
     student_id = models.OneToOneField(StudentID , related_name="depart" ,on_delete=models.CASCADE) #one to one field isley use kri h kyuki id unique honi chahiye
     student_name = models.CharField(max_length=100)
     student_email = models.EmailField(unique=True) #mtlb agr abc@gmail.com bna di toh yeh apn vaapis nhi bna skte fir bnao toh dusri hi bnao
     student_age = models.IntegerField(default=18)
     student_address= models.TextField()
     

     def __str__(self):
        return self.student_name 

     class Meta:
            ordering = ['student_name']
            verbose_name ='student'   



# SUBJECT MODEL
class Subject(models.Model):
     subject_name = models.CharField(max_length=100)

     def __str__(self):
       return self.subject_name


# SUBJECTMARKS MODEL
class Subjectmarks(models.Model):
     student= models.ForeignKey(Student , related_name="studentmarks" ,on_delete=models.CASCADE)
     subject_name = models.ForeignKey(Subject , related_name="studentmarks",on_delete=models.CASCADE)
     marks = models.IntegerField()
     def __str__(self):
      return f'{self.student.student_name} {self.subject_name.subject_name}'
class Meta:
        unique_together = ['student','subject_name']



# STUDENTAGE MODEL
class Studentage(models.Model):
    student_age = models.IntegerField()

    def __str__(self):
       return self.student_age

