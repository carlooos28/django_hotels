from django.http import HttpResponse

# Utilities 
from datetime import datetime 

import json 

def test1(request):
  return HttpResponse('Soy Nivel Pro Colombia!')

now = datetime.now()

def test2(request):
  return HttpResponse('Ôh, Test {now}'.format(
    now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
  ))

def hi(request):
  # debugger
  # import pdb; pdb.set_trace()
  numbers = request.GET['numbers']
  return HttpResponse(str(numbers))

def test3(request):
  numbers = [int(i) for i in request.GET['numbers'].split(',')]
  sorted_ints = sorted(numbers)
  # import pdb; pdb.set_trace()
  data = {
    'status': 'Ok',
    'numbers': sorted_ints,
    'message': 'Request successfully'
  }
  return HttpResponse(
    json.dumps(data, indent=4),
    content_type='application/json'
  )

def test4(request, name, country):
  if country == "colombia":
    message = 'Eres {}, de nacionalidad Colombiana'.format(name)
  else:
    message = '{}, No Eres de nacionalidad Colombiana'.format(name) 
  return HttpResponse(message)
