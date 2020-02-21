#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
# var for batches dict
  batches = []

# iterate over recipe 
  for key in recipe.keys():
    # if key exist and enough igredients for 1 batch,
    if key in ingredients and ingredients[key] >= recipe[key]:
      # save batch count to ingredient batch list
      batches.append(ingredients[key] // recipe[key])
    else:
      return 0
  # find smallest batch number
  return min(batches)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
