from django.contrib import admin

from .models import Category, Question, Answer

admin.site.register(Category)

class AnswerAdmin(admin.StackedInline):  # it can list all the ForeignKey relationship

    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
