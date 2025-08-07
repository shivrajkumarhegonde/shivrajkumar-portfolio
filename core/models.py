# core/models.py
from django.db import models

class Project(models.Model):
    """
    Represents a single project in the portfolio.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200) # e.g., "Django, React, PostgreSQL"
    image = models.ImageField(upload_to='project_images/')
    demo_link = models.URLField(blank=True, null=True) # Link to the live project
    github_link = models.URLField(blank=True, null=True) # Link to the source code
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_technologies(self):
        """
        Splits the technologies string into a list and trims whitespace
        from each technology name.
        """
        # This will split 'Python, Django, HTML' into ['Python', 'Django', 'HTML']
        return [tech.strip() for tech in self.technologies.split(',')]

    def __str__(self):
        return self.title