def add_time(start, duration, day = None):
  days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7:"Sunday"}
  if day != None:
    day = day.capitalize()

  split = start.replace(':', ' ')
  time = split.split()
  hour, minutes = int(time[0]), int(time[1])
  # converting the original hour and minutes

  change = duration.split(":")
  hour_change, minutes_change = int(change[0]), int(change[1])
  # converting the hour and minutes that change the original time
  
  if time[2] == "PM":
    hour = hour + 12
  # converting PM numbers to a 24 hour clock
  total_hours = hour + hour_change
  if minutes + minutes_change > 60:
     total_hours += 1
    # accounting for the extra hour when minutes go above 60
  total_days = total_hours / 24
  if total_days > 1:
    total_days = round(total_days)
    # rounding down for the total days
  final_hours = str(total_hours % 12)
  if final_hours == "0":
    final_hours = "12"
  # converting to 12 hour clock
  time_of_day = total_hours % 24
  if time_of_day >= 12:
    am_pm = " PM"
  else:
    am_pm = " AM"
  # AM/PM check
  final_minutes = str((minutes + minutes_change) % 60)
  # conversion back to 60 minutes
  str_days = ""
  if total_days == 1:
    str_days = " (next day)"
  elif total_days > 1:
    str_days = " ({} days later)".format(total_days)
  # (n days later) strings
  if int(final_minutes) < 10:
    final_minutes = "0" + final_minutes
  # converts any minutes less than 10 to have 0 beforehand
  final_day = day
  for x, y in days.items():
    if day == y and total_days >= 1:
      final_num = (x + total_days) % 7
      # loops through dictionaries via modulus function
      if final_num == 0:
        final_day = days[7]
        # accounts for 0/Sunday issue
      else:
        final_day = days[final_num]
  if day == None:
    new_time = final_hours + ":" + final_minutes + am_pm + str_days
  else:
    new_time = final_hours + ":" + final_minutes + am_pm + ", " + final_day + str_days
  return new_time