# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
from threading import Thread
from bs4 import BeautifulSoup
from .models import SiteAdminModel
from django.http import HttpResponse, JsonResponse
from django.utils import timezone


try:
    from queue import Queue
    from urllib.request import urlopen, Request
except ImportError:
    from Queue import Queue
    from urllib2 import urlopen, Request

threads = []
sites_queue = Queue()


def parse_site_and_upload_to_db(site):
    seconds_to_sleep = site.timeshift_for_parsing
    time.sleep(seconds_to_sleep)
    parsing_time = timezone.now()
    try:
        req = Request(site.site_url, headers={'User-Agent': 'Mozilla/5.0'})
        get = urlopen(req).read().decode('utf-8', 'ignore')
        dom = BeautifulSoup(get, 'html.parser')
        html = dom.text
        site_title = dom.findAll('title')
        site_header = dom.findAll('h1')
        site_encoding = dom.findAll('meta', {'http-equiv': True})

        parsed_info = {
            'site_url': site.site_url,
            'site_title': site_title[0].text if site_title else None,
            'site_header': site_header[0].text if site_header else None,
            'site_encoding': site_encoding[0]['content'] if site_encoding else None,
            'parsing_time': parsing_time.strftime('%Y-%m-%d %H:%M:%S'),
            'parsing_complete': site.parsing_complete,
        }

        SiteAdminModel.objects.filter(id=site.id).update(
                parsing_time=parsing_time, parsing_complete=True, site_title=parsed_info['site_title'],
                site_header=parsed_info['site_header'], site_encoding=parsed_info['site_encoding']
            )
        sites_queue.put({'id': site.id, 'data': parsed_info})
    except Exception as e:
        sites_queue.put({'id': site.id, 'data': {'parsing_complete': 'wrong url'}})
    


def start_parsing(request):
    if sites_queue.empty() and not threads:
        for site in SiteAdminModel.objects.all():
            thread = Thread(target=parse_site_and_upload_to_db, args=(site,))
            threads.append(thread)
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=204)

def get_new_info(request):
    if not sites_queue.empty():
        result_list = []
        while not sites_queue.empty():
            result_list.append(sites_queue.get())
        return JsonResponse(result_list, safe=False)
    elif not any([thread.isAlive() for thread in threads]):
        threads[:] = []
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=202)
