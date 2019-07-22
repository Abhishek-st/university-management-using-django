from django.db import models, transaction


class Department(models.Model):
    dnum = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=20)

    def __str__(self):
        return self.dname


class RoomDetails(models.Model):
    roomno = models.PositiveSmallIntegerField(primary_key=True)
    type = models.CharField(max_length=10)
    fees = models.DecimalField(decimal_places=2, max_digits=10)
    nbeaded = models.PositiveSmallIntegerField()


class Hostel(models.Model):
    hid = models.AutoField(primary_key=True)
    block = models.CharField(max_length=10)
    roommo = models.ForeignKey(RoomDetails, on_delete=models.CASCADE)


class Student(models.Model):
    regno = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=30)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    semester = models.PositiveSmallIntegerField(default=1)
    branch = models.ForeignKey(Department, on_delete=models.CASCADE, default=123)
    father = models.CharField(max_length=30, default='non')
    fathers_occupation = models.CharField(max_length=50, default='non')
    mother = models.CharField(max_length=30, default='non')
    mothers_occupation = models.CharField(max_length=50, default='non')
    house_no = models.SmallIntegerField(default=123)
    locality = models.CharField(max_length=200, default='non')
    city = models.CharField(max_length=50, default='non')
    state = models.CharField(max_length=100, default='non')
    pin = models.IntegerField(default=123456)
    hid = models.ForeignKey(Hostel, on_delete=models.CASCADE, blank=True, null=True)
    img = models.ImageField(default="{%static 'vit\images\pw.jpg'%}")

    def __str__(self):
        return self.regno


class Course(models.Model):
    cid = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=30)
    credit = models.SmallIntegerField()

    def __str__(self):
        return self.cname


class Enrolled(models.Model):
    cid = models.ForeignKey(Course, on_delete=models.CASCADE)
    regno = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.PositiveSmallIntegerField(default=1)
    cat1 = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    cat2 = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    ass1 = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    ass2 = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    ass3 = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    fat = models.DecimalField(decimal_places=2, max_digits=6, default=0)


    class Meta:
        unique_together = ('cid', 'regno')



class Offers(models.Model):
    dnum = models.ForeignKey(Department, on_delete=models.CASCADE)
    cid = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('dnum', 'cid')


class Faculty(models.Model):
    fid = models.CharField(max_length=15, primary_key=True)
    fname = models.CharField(max_length=30)
    designation = models.CharField(max_length=20)
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    dnum = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.fname


class Teaches(models.Model):
    fid = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    cid = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('fid', 'cid')


class Library(models.Model):
    memid = models.CharField(max_length=15, primary_key=True)
    lname = models.CharField(max_length=30)

    def __str__(self):
        return self.lname


class Book(models.Model):
    bookid = models.IntegerField(primary_key=True)
    bname = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    available = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.bname


class Borrow(models.Model):
    memid = models.ForeignKey(Library, on_delete=models.CASCADE)
    bookid = models.ForeignKey(Book, on_delete=models.CASCADE)
    returndate = models.DateField(null=True, blank=True)
    issuedate = models.DateField()
    duedate = models.DateField()

    class Meta:
        unique_together = ('memid', 'bookid')


class Class(models.Model):
    clid = models.IntegerField(primary_key=True)
    roomno = models.PositiveSmallIntegerField()
    startime = models.TimeField()
    endtime = models.TimeField()
    day = models.CharField(max_length=10)
    cid = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.clid)


class Take(models.Model):
    regno = models.ForeignKey(Student, on_delete=models.CASCADE)
    clid = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    attendence = models.CharField(max_length=9, choices=(('present', 'present'), ('absent', 'absent')))

    class Meta:
        unique_together = ('clid', 'regno')


class FeesInf(models.Model):
    feid = models.IntegerField(primary_key=True)
    fename = models.CharField(max_length=25)

    def __str__(self):
       return self.fename


class StdentMob(models.Model):
    mobile = models.IntegerField()
    regno = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('mobile', 'regno')


class Outing(models.Model):
    regno = models.ForeignKey(Student, on_delete=models.CASCADE)
    out = models.DateTimeField()
    ent = models.DateTimeField()
    reason = models.TextField()
    place = models.CharField(max_length=30)


class PreReq(models.Model):
    cid = models.ForeignKey(Course, on_delete=models.CASCADE)
    preid = models.IntegerField()


class Account(models.Model):
    regno = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
    tution = models.IntegerField(blank=True, null=True, default=0)
    hostel = models.IntegerField(blank=True, null=True, default=0)
    mess = models.IntegerField(blank=True, null=True, default=0)
    hdues = models.SmallIntegerField(blank=True, null=True)
    ldues = models.SmallIntegerField(blank=True, null=True)


class Material(models.Model):
    cid = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default="abc")
    fid = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    mat = models.FileField(null=True, blank=True)

    class Meta:
        unique_together = ('fid', 'cid', 'mat')
