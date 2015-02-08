#!/usr/bin/python

# This script will replace an input in django crispy forms with a d3 autocomplete

from cognitiveatlas import views

# Here is the django field we are going to substitute
django_field = "contrast_definition_cogatlas"

# We already will have bootstrap in the page
include_bootstrap = False

# generate the code to add to form page
html_snippet = views.contrast_selector_django_crispy_form(django_field=django_field,include_bootstrap=False)
