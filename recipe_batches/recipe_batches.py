#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
# var for batches dict
  batches = {}

# iterate over recipe 
  for key in recipe.keys():
    if key in ingredients and ingredients[key] > recipe[key]:
      print('batch is possible')
      batches[key] = 
    else: 
      print('batch is not possible')
      return 0

  # if key doesnt exist, return 0
  # elif recipe key >= ingredient, return 0

recipe_batches({ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 198, 'butter': 52, 'cheese': 10 })
# recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 })

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
