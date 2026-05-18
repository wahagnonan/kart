from django.db import models


class Question(models.Model):
    texte = models.TextField(verbose_name="Texte de la question")
    ordre = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordre']

    def __str__(self):
        return f"Q{self.ordre} — {self.texte[:60]}"


class Artisan(models.Model):
    contact = models.CharField(max_length=255, verbose_name="Contact")
    ville = models.CharField(max_length=100, verbose_name="Ville")
    metier = models.CharField(max_length=100, verbose_name="Métier")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.metier} — {self.ville}"


class Reponse(models.Model):
    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE, related_name='reponses')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='reponses')
    contenu = models.TextField(blank=True)

    class Meta:
        unique_together = ('artisan', 'question')
        ordering = ['question__ordre']

    def __str__(self):
        return f"{self.artisan} → Q{self.question.ordre}"
