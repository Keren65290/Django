from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe


def recipes(request):
    if request.method == 'POST':
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        Recipe.objects.create(
            recipe_image=recipe_image,
            recipe_name=recipe_name,
            recipe_description=recipe_description,
        )
        return redirect('recipe_list')  # Redirect to the recipe list view

    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(
            recipe_name__icontains=request.GET.get('search'))

    context = {'recipes': queryset}
    return render(request, 'recipe/recipes.html', context)


def delete_recipe(request, id):
    queryset = get_object_or_404(Recipe, id=id)
    queryset.delete()
    return redirect('recipe_list')  # Redirect back to the recipe list view


def update_recipe(request, id):
    queryset = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        # Update the fields of the recipe
        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        # Only update the recipe_image if a new one is uploaded
        if recipe_image:
            queryset.recipe_image = recipe_image

        # Save the updated recipe to the database
        queryset.save()

        # Redirect to the recipe list after updating
        return redirect('recipe_list')  # No namespace here

    # If the request method is not POST, render the update form with the existing recipe
    context = {'recipe': queryset}
    return render(request, 'recipe/update_recipe.html', context)

