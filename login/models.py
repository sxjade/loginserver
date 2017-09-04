# -*- coding:utf-8 -*-
from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=20,primary_key=True)
	password = models.CharField(max_length=20)
	opendate = models.DateTimeField('create date',auto_now_add=True) 
	lastlogonDate = models.DateTimeField('last login',auto_now_add=True) 
	userType = models.IntegerField(default = 1)  #用户账户类型
	
	def __str__(self):
		return self.username
	
class UserCtpAccount(models.Model):
	username = models.ForeignKey('User',primary_key=True)
	ctpTradeIp = models.CharField(max_length=40)
	ctpQuoteIp = models.CharField(max_length=40)
	ctpTradePort = models.IntegerField(default = 1)
	ctpQuotePort = models.IntegerField(default = 1)
	ctpBroker = models.IntegerField(default = 1)
	ctpUserName = models.CharField(max_length=20)
	ctpUserPassword = models.CharField(max_length=20)
	
	def __str__(self):
		return self.username.username
	
	
