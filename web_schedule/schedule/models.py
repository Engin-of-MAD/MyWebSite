from django.db import models


class Admins(models.Model):
    adm_id = models.IntegerField(blank=True, null=True)
    post_id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(db_column='First_Name', max_length=32, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=12, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admins'


class Auds(models.Model):
    aud_id = models.AutoField(primary_key=True)
    aud = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)
    info = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auds'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Days(models.Model):
    id_day = models.AutoField(primary_key=True)
    day = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'days'

    def __str__(self):
        return self.day


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    id_employee = models.AutoField(primary_key=True)
    post_id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(db_column='First_Name', max_length=32, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=32, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    specialization = models.CharField(db_column='Specialization', max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=12, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Lessons(models.Model):
    ls_id = models.IntegerField(primary_key=True)
    tchr_id = models.IntegerField(blank=True, null=True)
    name_lesson = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)
    info = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lessons'


class Post(models.Model):
    post_id = models.IntegerField(blank=True, null=True)
    post = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)
    responsibility = models.TextField(db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'


class RepBase(models.Model):
    rep_id = models.AutoField(primary_key=True)
    stud_id = models.IntegerField(blank=True, null=True)
    aud_id = models.IntegerField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rep_base'


class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    lesson_id = models.IntegerField(blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)
    day_id = models.IntegerField(blank=True, null=True)
    type_lesson_id = models.IntegerField(blank=True, null=True)
    aud_id = models.IntegerField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule'
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'
        ordering = ['day_id', 'time', 'aud_id']

    def __str__(self):
        return str(self.day_id)

    @classmethod
    def decode(cls):
        coded_data = []
        decoded_data = []
        data = cls.objects.all()

        for item_data in data:
            coded = {
                'lesson_id': None,
                'teacher_id': None,
                'day_id': None,
                'type_lesson_id': None,
                'aud_id': None,
                'time': None
            }

            coded['lesson_id'] = item_data.lesson_id
            coded['teacher_id'] = item_data.teacher_id
            coded['day_id'] = item_data.day_id
            coded['type_lesson_id'] = item_data.type_lesson_id
            coded['aud_id'] = item_data.aud_id
            coded['time'] = item_data.time

            coded_data.append(coded)

        for item_data in coded_data:
            decoded = {'lesson': None, 'teacher': None, 'day': None,
                       'type_lesson': None, 'aud': None, 'time': None}

            decoded['lesson'] = Lessons.objects.get(pk=item_data['lesson_id']).name_lesson
            first_name = Employee.objects.filter(post_id=1).get(pk=item_data['teacher_id']).first_name
            last_name = Employee.objects.filter(post_id=1).get(pk=item_data['teacher_id']).last_name
            fio = first_name + " " + last_name
            decoded['teacher'] = fio
            decoded['day'] = Days.objects.get(pk=item_data['day_id']).day
            decoded['type_lesson'] = TypesLessons.objects.get(pk=item_data['type_lesson_id']).type_lesson
            decoded['aud'] = Auds.objects.get(pk=item_data['aud_id']).aud
            decoded['time'] = item_data['time']
            decoded_data.append(decoded)

        return decoded_data

    @classmethod
    def sort_schedule(cls, data: list):
        sorted_data = []
        for item_data in data:
            if item_data['day'] == "Понедельник":
                sorted_data.append(item_data)

        for item_data in data:
            if item_data['day'] == "Вторник":
                sorted_data.append(item_data)

        for item_data in data:
            if item_data['day'] == "Среда":
                sorted_data.append(item_data)

        for item_data in data:
            if item_data['day'] == "Четверг":
                sorted_data.append(item_data)

        for item_data in data:
            if item_data['day'] == "Пятница":
                sorted_data.append(item_data)

        for item_data in data:
            if item_data['day'] == "Суббота":
                sorted_data.append(item_data)

        for item_data in data:
            if item_data['day'] == "Суббота":
                sorted_data.append(item_data)

        for item_data in data:
            if item_data['day'] == "Воскресенье":
                sorted_data.append(item_data)

        return sorted_data


class Students(models.Model):
    stud_id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(db_column='First_Name', max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'


class TypesLessons(models.Model):
    tpls_id = models.AutoField(primary_key=True)
    type_lesson = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    long = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types_lessons'


class TypesOrgs(models.Model):
    orgs = models.CharField(max_length=64)
