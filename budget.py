class Category:
  def __init__(self, name):   
    self.ledger = []
    self.name = name
    #declaring variable and list in constructor
  def deposit(self, nums, desc=""):
    self.ledger.append({"amount": nums, "description": desc})
  def withdraw(self, nums, desc=""):
    self.nums = nums * -1
    if self.check_funds(nums) is True:
      self.ledger.append({"amount": self.nums, "description": desc})
      return True
    else:
      return False
    # withdrawing via check funds method check
  def get_balance(self):
    values = 0
    for i in range(len(self.ledger)):
      values += self.ledger[i]["amount"]
    return values
  def transfer(self, amount, categories):
    if self.check_funds(amount) is True:
      self.withdraw(amount, "Transfer to {}".format(categories.name))
      categories.deposit(amount, "Transfer from {}".format(self.name))
      return True
    else:
      return False
  def check_funds(self, amount):
    if self.get_balance() < amount:
      return False
    else:
      return True
      # example of using method in method
  def __str__(self):
    display_name = self.name.center(30, '*')
    # centers the name within *s
    display = display_name + "\n"
    for i in range(len(self.ledger)):
      row = f'{self.ledger[i]["description"]:23.23}{self.ledger[i]["amount"]:7.2f}'
      # limits how much of the values are shown
      display += row + "\n"
    total = self.get_balance()  
    display += "Total: {}".format(total)
    return display
    # determining what is printed when the object is included in a statement
def create_spend_chart(categories):
  num_spent = {}
  total = 0
  max_length = 0
  chart = "Percentage spent by category\n"
  # declraing variables and the top of the bar chart
  
  for category in categories:
    category_total = 0
    if len(category.name) > max_length:
      max_length = len(category.name)
      # working out max length for category names loop
    for i in range(len(category.ledger)):
      if category.ledger[i]["amount"] < 0:
        category.ledger[i]["amount"] = category.ledger[i]["amount"] * -1
        category_total += category.ledger[i]["amount"]
        num_spent[category.name] = category_total
        # making the withdrawal amounts positive
  for j in num_spent:
    total += num_spent[j]
  new_num_spent = {}
  for k in num_spent:
    num_spent[k] = (num_spent[k] / total) * 100 
    new_num_spent[k] = round(num_spent[k] - (num_spent[k] % 10))
    # converting the category values to a percentage and rounding down to nearest 10
  
  for l in range(100, -1, -10):
    if l == 100:
      chart += str(l) + "|"
    elif l == 0:
      chart += "  " + str(l) + "|"
    else:
      chart += " " + str(l) + "|"
    for m in new_num_spent:
      if new_num_spent[m] >= l:
        chart += " o "
      else:
        chart += "   "
    if l >= 0:
      chart += " \n"
    else:
      break
    # looping through the graph values and printing the Y axis and the values for each category through the use of 'o'
  chart += "    " + (len(categories) * 3) * "-" + "-" + "\n"
  for n in range(max_length):
    chart += 4 * " "
    for o in new_num_spent.keys():
      if len(o) > n:
        chart += " " + o[n] + " " 
      else:
        chart += "   "
    if n == max_length - 1:
      chart += " "
      break
    else:
      chart += " \n"
  return chart
  # creates the dash line and the categories and spaces underneath, as well as end of string check to ensure no extra end line