from decimal import Decimal
from django.conf import settings
from veb.models import Coors, FavoriteItem


class Favorite(object):
    def __init__(self, request):
        self.session = request.session
        favorite = self.session.get(settings.FAVORITE_SESSION_ID)
        if not favorite:
            favorite = self.session[settings.FAVORITE_SESSION_ID] = {}
        self.favorite = favorite

    def add_favorite(self, course):
        course = str(course.id)
        if course not in self.favorite:
            self.favorite[course] = {'course': course}
        self.save()

    def save(self):
        self.session[settings.FAVORITE_SESSION_ID] = self.favorite
        self.session.modified = True

    def __iter__(self):
        course_id = self.favorite.keys()
        courses = Coors.objects.filter(id=course_id)
        for coors in courses:
            self.favorite[str(coors.id)]['courses'] = coors

    def clear(self):
        del self.session[settings.FAVORITE_SESSION_ID]
        self.session.modified = True

    def remove(self, course):
        course_id = str(course.id)
        if course_id in self.favorite:
            del self.favorite[course_id]
            self.save()
