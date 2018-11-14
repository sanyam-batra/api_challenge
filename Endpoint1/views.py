from django.shortcuts import render
from rest_framework.views import APIView
import json
from django.http import HttpResponse
import datetime
import random
import time
# Create your views here.


get_count = 0
post_count = 0
put_count = 0
del_count = 0
avg_response_get = 0
avg_response_post = 0
avg_response_put = 0
avg_response_delete = 0


class Json_response(APIView):

    def get(self, request):
        global get_count,avg_response_get
        get_count += 1
        req_time = datetime.datetime.now()
        method = request.method
        header = request.META
        path = request.path
        duration = random.randint(15, 30)
        avg_response_get=(avg_response_get+duration)/get_count
        x = {
            "time": req_time,
            "method": method,
            "header": header,
            "path": path,
            "duration": duration
        }

        y = json.dumps(x, indent=4, sort_keys=True, default=str)
        time.sleep(duration)
        return HttpResponse(y)

    def post(self, request):
        global post_count,avg_response_post
        post_count += 1
        req_time = datetime.datetime.now()
        method = request.method
        header = request.META
        path = request.path
        duration = random.randint(15, 30)
        avg_response_post=(avg_response_post+duration)/post_count
        x = {
            "time": req_time,
            "method": method,
            "header": header,
            "path": path,
            "duration": duration
        }
        y = json.dumps(x, indent=4, sort_keys=True, default=str)
        time.sleep(duration)
        return HttpResponse(y)

    def put(self,request):
        global put_count,avg_response_put
        put_count += 1
        req_time = datetime.datetime.now()
        method = request.method
        header = request.META
        path = request.path
        duration = random.randint(15, 30)
        avg_response_put = (avg_response_put+duration)/put_count
        x = {
            "time": req_time,
            "method": method,
            "header": header,
            "path": path,
            "duration": duration
        }
        y = json.dumps(x, indent=4, sort_keys=True, default=str)
        time.sleep(duration)
        return HttpResponse(y)

    def delete(self,request):
        global del_count,avg_response_delete
        del_count+=1
        req_time = datetime.datetime.now()
        method = request.method
        header = request.META
        path = request.path
        duration = random.randint(15, 30)
        avg_response_delete = (avg_response_delete+duration)/del_count
        x = {
            "time": req_time,
            "method": method,
            "header": header,
            "path": path,
            "duration": duration
        }
        y = json.dumps(x, indent=4, sort_keys=True, default=str)
        time.sleep(duration)
        return HttpResponse(y)


def req_count(request):
    global get_count,post_count,put_count,del_count
    total_count = get_count+post_count+put_count+del_count
    stats={'total_count':total_count,'get_count':get_count,'post-count':post_count,'put_count':put_count,'delete_count':del_count,
           'average_get_response':avg_response_get,'average_post_response':avg_response_post,'average_put_response':avg_response_put,'average_delete_response':avg_response_delete}
    return HttpResponse(json.dumps(stats))

