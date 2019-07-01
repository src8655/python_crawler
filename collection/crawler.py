import ssl
import sys
from urllib.request import Request, urlopen
from datetime import datetime


def crawling(url='',
             encoding='utf-8',
             err=lambda e: print('{0} : {1}'.format(e, datetime.now()), file=sys.stderr),
             proc1=lambda data: data,
             proc2=lambda data: data):
    try:
        request = Request(url)

        context = ssl._create_unverified_context()
        response = urlopen(request, context=context)
        print('{0}: success for request [{1}]'.format(datetime.now(), url))

        result = proc2(proc1(response.read().decode(encoding, errors='replace')))

        return result
    except Exception as e:
        err(e)
        return False
