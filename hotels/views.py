"""Hotels views."""

# Django
# from django.http import HttpResponse

# Utilities
from datetime import datetime

from django.shortcuts import render

hotels = [
    {
        'city': 'Bogota',
        'user': {
          'administrator': 'Daniel Morales',
        },        
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'city': 'Cartagena',
        'user': {
          'administrator': 'Camilo Torres',
        },        
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'city': 'Cali',
        'user': {
          'administrator': 'Daniela Torres',
        },                        
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076',
    }
]


def list_hotels(request):
    """List existing hotels."""
    content = []
    for hotel in hotels:
        content.append("""
            <p><strong>{city}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
        """.format(**hotel))
    return HttpResponse('<br>'.join(content))

def list_hotels_1(request):
  return render(request, 'feed.html', {'hotels': hotels })













