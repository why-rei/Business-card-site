from django.shortcuts import render, redirect
from django.views import View

from .models import Resumes


class ResumeView(View):
    """Вывод пользователя"""

    def get(self, request, lang):
        resume = Resumes.objects.select_related('template', 'template__lang', 'resume_user__contacts'). \
            prefetch_related('resume_user__projects', 'resume_user__soft_skills', 'resume_user__hard_skills'). \
            get(lang=lang)
        template = resume.template
        user = resume.resume_user
        return render(request, "index.html", {'template': template, 'user': user})


def redirect_to_resume(request):
    """Redirect to resume page"""

    return redirect("/ru/resume")
