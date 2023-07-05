from django.db import models


class ResumeLangs(models.Model):
    class Meta:
        verbose_name = "Resume lang"
        verbose_name_plural = "Resume langs"

    lang = models.SlugField(primary_key=True)

    def __str__(self):
        return self.lang


class ResumeContacts(models.Model):
    class Meta:
        verbose_name = "Resume contact"
        verbose_name_plural = "Resume contacts"

    lang = models.OneToOneField(ResumeLangs, on_delete=models.PROTECT, primary_key=True)
    gmail = models.CharField(max_length=30)
    tel = models.CharField(max_length=20)
    github_href = models.CharField(max_length=100)
    social = models.CharField(max_length=20)
    social_href = models.CharField(max_length=100)

    def __str__(self):
        return self.lang.__str__()


class ResumeProjects(models.Model):
    class Meta:
        verbose_name = "Resume project"
        verbose_name_plural = "Resume projects"

    lang = models.ForeignKey(ResumeLangs, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    github = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.lang} - {self.name}'


class ResumeSkillsSoft(models.Model):
    class Meta:
        verbose_name = "Resume soft skill"
        verbose_name_plural = "Resume soft skills"

    lang = models.ForeignKey(ResumeLangs, on_delete=models.PROTECT)
    skill = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.lang} - {self.skill}'


class ResumeSkillsHard(models.Model):
    class Meta:
        verbose_name = "Resume hard skill"
        verbose_name_plural = "Resume hard skills"

    skill = models.CharField(max_length=50)

    def __str__(self):
        return self.skill


class ResumeUsers(models.Model):
    class Meta:
        verbose_name = "Resume user"
        verbose_name_plural = "Resume users"

    lang = models.OneToOneField(ResumeLangs, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    soft_skills = models.ManyToManyField(ResumeSkillsSoft, verbose_name="Soft skills")
    hard_skills = models.ManyToManyField(ResumeSkillsHard, verbose_name="Hard skills")
    projects = models.ManyToManyField(ResumeProjects, verbose_name="Projects")
    contacts = models.ForeignKey(ResumeContacts, on_delete=models.PROTECT)

    def __str__(self):
        return self.lang.__str__()


class ResumeTemplates(models.Model):
    class Meta:
        verbose_name = "Resume template"
        verbose_name_plural = "Resume templates"

    lang = models.OneToOneField(ResumeLangs, on_delete=models.PROTECT, primary_key=True)
    about = models.CharField(max_length=15)
    skills = models.CharField(max_length=15)
    skills_text = models.CharField(max_length=50)
    soft_skills = models.CharField(max_length=50)
    hard_skills = models.CharField(max_length=50)
    projects = models.CharField(max_length=15)
    projects_text = models.CharField(max_length=50)
    contacts = models.CharField(max_length=15)
    contacts_text = models.CharField(max_length=50)
    btn_text = models.CharField(max_length=15)

    def __str__(self):
        return self.lang.__str__()


class Resumes(models.Model):
    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"

    lang = models.OneToOneField(ResumeLangs, on_delete=models.PROTECT, primary_key=True)
    template = models.ForeignKey(ResumeTemplates, on_delete=models.PROTECT)
    resume_user = models.ForeignKey(ResumeUsers, on_delete=models.PROTECT)

    def __str__(self):
        return self.lang.__str__()
