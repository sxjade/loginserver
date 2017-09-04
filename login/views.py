# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import json
from .models import User,UserCtpAccount
import datetime

def index(request):
	return HttpResponse("test ok")
# Create your views here.

def getUserCtpAccount(userObj):
	result = {}
	try:
		ctpAccount = UserCtpAccount.objects.get(username=userObj)
		result['ctpTradeIp'] = ctpAccount.ctpTradeIp
		result['ctpQuoteIp'] = ctpAccount.ctpQuoteIp
		result['ctpQuoteIp'] = ctpAccount.ctpQuoteIp
		result['ctpTradePort'] = ctpAccount.ctpTradePort
		result['ctpQuotePort'] = ctpAccount.ctpQuotePort
		result['ctpBroker'] = ctpAccount.ctpBroker
		result['ctpUserName'] = ctpAccount.ctpUserName
		result['ctpUserPassword'] = ctpAccount.ctpUserPassword
	except UserCtpAccount.DoesNotExist:
		return None
	return result
	
def login(request):
	result = {}
	password = request.POST.get('password','')
	username = request.POST.get('username','')
	
	password = request.GET.get('password','')
	username = request.GET.get('username','')
	print(username,password)
	if(username==''):
		result['status'] = 'error'
		result['errmsg'] = 'empty username'
		return HttpResponse(json.dumps(result))
	
	try:
		user = User.objects.get(username=username)
		if(user.password == password):
			result['lastLoginTime'] = user.lastlogonDate.strftime("%Y-%m-%d %H:%M:%S")
			user.lastlogonDate = datetime.datetime.now()
			result['usertype'] = user.userType
			result['status'] = 'ok'
			
			ctpResult = getUserCtpAccount(user)   #这里取出ctpaccount信息
			if ctpResult != None :
				result['ctpAccount'] = ctpResult
			
			user.save()
			return HttpResponse(json.dumps(result))
	except User.DoesNotExist:
		result['status'] = 'error'
		result['errmsg'] = 'username not exist'
		return HttpResponse(json.dumps(result))
	
	return HttpResponse(json.dumps(result))

def insetuser(request):
	
	if request.method == 'GET':
		password = request.GET.get('password')
		username = request.GET.get('username')
        
        user = User(password=password,username=username)
        user.save()
	return HttpResponse('insert ok')
	
