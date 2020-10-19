from django.contrib import admin
from myapp.models import board, post, postblog

admin.site.register(board)

#admin.site.register(post)


class postAdmin(admin.ModelAdmin):
    list_display=('id', 'ptitle', 'pcontent', 'purl')
    
admin.site.register(post, postAdmin)

class postblogAdmin(admin.ModelAdmin):
    list_display=('id', 'pbtitle', 'pbcontent')

admin.site.register(postblog, postblogAdmin)
