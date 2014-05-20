from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from RecipeBook.models import Recipe

recipes = Blueprint('recipes', __name__, template_folder='templates')


class ListView(MethodView):

    def get(self):
        recipes = Recipe.objects.all()
        return render_template('recipes/list.html', recipes=recipes)


class DetailView(MethodView):

    def get(self, slug):
        recipe = Recipe.objects.get_or_404(slug=slug)
        return render_template('recipes/detail.html', recipe=recipe)


# Register the urls
recipes.add_url_rule('/', view_func=ListView.as_view('list'))
recipes.add_url_rule('/<slug>/', view_func=DetailView.as_view('detail'))
