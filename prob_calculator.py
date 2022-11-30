import copy
import random

class Hat:
  def __init__(self, **kwargs):
    # kwargs can be swapped out for any name, just keeping as a reference
    self.contents = []
    self.counter = 0
    for key, value in kwargs.items():
      while self.counter < value:
        self.contents.append(key)
        self.counter += 1
      self.counter = 0
      # keyword arguments are converted into list of strings of colours
  def draw(self, num):
    if num > len(self.contents):
      self.drawn = copy.deepcopy(self.contents)
    else:
      self.drawn = []
      self.counters = 0
      while num > self.counters:
        chosen_hat = random.choice(self.contents)
        self.drawn.append(chosen_hat)
        self.contents.remove(chosen_hat)
        self.counters += 1
    return self.drawn
    # balls are randomly chosen and appended to drawn list + removed from contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  counter = 0
  # counter for experiment matches tallied at the end
  for i in range(num_experiments):
    experiment_hats = copy.deepcopy(hat) # avoids mutation of original
    new_list = []
    newdict = {}
    result = experiment_hats.draw(num_balls_drawn)
    # result of draw method
    for items in result:
      if items in new_list:
        continue
      else:
        new_list.append(items) # new_list is distinct colours
        j = 0
        counts = 0
        num = 0
    for elements in new_list:
      while counts < len(result):
        if elements in result[j]:
          num += 1
          j += 1
          counts += 1
        else:
          j += 1
          counts += 1
      newdict[elements] = num
      num = 0
      j = 0
      counts = 0
    colour_num_check = 0
    # creating dict from result to comapre with expected_balls
    for keys in expected_balls.keys():
      if keys in newdict.keys():
        if expected_balls[keys] > newdict[keys]: 
          break
        else:
          colour_num_check += 1
    # conditionals to compare colour values
    if colour_num_check == len(expected_balls):
      counter += 1
    # counter for expected_balls match in experiment
  probability = float(counter / num_experiments)
  return probability
