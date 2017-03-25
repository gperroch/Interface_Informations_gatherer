# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from __future__ import unicode_literals

from django.db import models


class auth_group(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class auth_group_permissions(models.Model):
    group = models.ForeignKey(auth_group, models.DO_NOTHING)
    permission = models.ForeignKey('auth_permission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'informations_gatherer.auth_group_permissions'
        unique_together = (('group', 'permission'),)


class auth_permission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('django_content_type', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class auth_user(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class auth_user_groups(models.Model):
    user = models.ForeignKey(auth_user, models.DO_NOTHING)
    group = models.ForeignKey(auth_group, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'informations_gatherer.auth_user_groups'
        unique_together = (('user', 'group'),)


class auth_user_user_permissions(models.Model):
    user = models.ForeignKey(auth_user, models.DO_NOTHING)
    permission = models.ForeignKey(auth_permission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'informations_gatherer.auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class django_admin_log(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('django_content_type', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(auth_user, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class django_content_type(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class django_migrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class django_session(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class locations(models.Model):
    idLocation = models.AutoField(db_column='idLocation', primary_key=True)  # Field name made lowercase.
    idPlace = models.ForeignKey('places', models.DO_NOTHING, db_column='idPlace', related_name='+')  # Field name made lowercase.
    idPerson = models.ForeignKey('persons', models.DO_NOTHING, db_column='idPerson', related_name='+')  # Field name made lowercase.
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class persons(models.Model):
    idPerson = models.AutoField(db_column='idPerson', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons'


class places(models.Model):
    idPlace = models.AutoField(db_column='idPlace', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'places'


class relationships(models.Model):
    idRelationship = models.AutoField(db_column='idRelationship', primary_key=True)  # Field name made lowercase.
    idPersonOne = models.ForeignKey(persons, models.DO_NOTHING, db_column='idPersonOne', related_name='+')  # Field name made lowercase.
    idPersonTwo = models.ForeignKey(persons, models.DO_NOTHING, db_column='idPersonTwo', related_name='+')  # Field name made lowercase.
    levelrelationship = models.IntegerField(db_column='levelRelationship', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'relationships'
