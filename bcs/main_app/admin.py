from django.contrib import admin

from .models import ResumeLangs, ResumeContacts, ResumeProjects, ResumeSkillsSoft, ResumeSkillsHard, ResumeUsers,\
                    ResumeTemplates, Resumes

admin.site.register(ResumeLangs)
admin.site.register(ResumeSkillsSoft)
admin.site.register(ResumeSkillsHard)
admin.site.register(ResumeContacts)
admin.site.register(ResumeProjects)
admin.site.register(ResumeUsers)
admin.site.register(ResumeTemplates)
admin.site.register(Resumes)
