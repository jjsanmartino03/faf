# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    year = models.BigIntegerField(unique=True)
    active = models.IntegerField()

    class Meta:
        db_table = 'categories'


class Crosses(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    local_team = models.ForeignKey('Teams', models.DO_NOTHING)
    visitor_team = models.ForeignKey('Teams', models.DO_NOTHING, related_name='crosses_visitor_team_set')

    class Meta:
        db_table = 'crosses'


class Matches(models.Model):
    id = models.BigAutoField(primary_key=True)
    cross = models.ForeignKey(Crosses, models.DO_NOTHING)
    local_team_category = models.ForeignKey('TeamCategories', models.DO_NOTHING)
    visitor_team_category = models.ForeignKey('TeamCategories', models.DO_NOTHING, related_name='matches_visitor_team_category_set')
    local_validation = models.ForeignKey('Validation', models.DO_NOTHING)
    visitor_validation = models.ForeignKey('Validation', models.DO_NOTHING, related_name='matches_visitor_validation_set')
    category = models.IntegerField()

    class Meta:
        db_table = 'matches'


class Players(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    team_category = models.ForeignKey('TeamCategories', models.DO_NOTHING)

    class Meta:
        db_table = 'players'


class TeamCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    team = models.ForeignKey('Teams', models.DO_NOTHING)
    category = models.ForeignKey(Categories, models.DO_NOTHING)

    class Meta:
        db_table = 'team_categories'


class Teams(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    logo_url = models.CharField(max_length=255)

    class Meta:
        db_table = 'teams'


class Validation(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=100)
    photo = models.CharField(max_length=255)

    class Meta:
        db_table = 'validation'


class ValidationPlayers(models.Model):
    id = models.BigAutoField(primary_key=True)
    player = models.ForeignKey(Players, models.DO_NOTHING)
    validation = models.ForeignKey(Validation, models.DO_NOTHING)

    class Meta:
        db_table = 'validation_players'
