from django.shortcuts import render


def todo_home_page(request):
    """Функция-представление главной(домашней) страницы"""
    return render(request, 'home.html',
                  {
                      'title': 'Главная'
                  })
