def add_time(start, duration, day = None):
  days = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
  if day != None:
    day = day.strip()
    day = day.capitalize()
  split = start.replace(':', ' ')
  time = split.split()
  upper_time = time[2].upper()
  hour, minutes = int(time[0]), int(time[1])
  # converting the original hour and minutes
  if upper_time == "PM" and hour != 12:
    hour += 12

  change = duration.split(":")
  hour_change, minutes_change = int(change[0]), int(change[1])
  # converting the hour and minutes that change the original time

  if minutes + minutes_change > 60:
    hour_change += 1
    # accounting for the extra hour when minutes go above 60
  total_days = (hour_change + hour) / 24
  total_days = int(total_days)
  # rounding down for the total days
  final_hours = (hour_change + hour) % 24
  if final_hours >= 12:
    am_pm = " PM"
    final_hours -= 12
  else:
    am_pm = " AM"
  if final_hours == 0:
    final_hours += 12
  final_hours = str(final_hours)

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
      final_day = days[final_num]
  if day == None:
    new_time = final_hours + ":" + final_minutes + am_pm + str_days
  else:
    new_time = final_hours + ":" + final_minutes + am_pm + ", " + final_day + str_days
  return new_time

if __name__=="__main__":
    while True:
        values = input("Please provide a start time and a duration with a colon separating the hours and minutes in each and a comma separating the two arguments: ")
        # Example input: 12:12PM, 17:15, Tuesday
        if values != "":
            break
    values_list = values.split(',')
    time = values_list[0]
    length = values_list[1]
    if len(values_list) > 2:
      day = values_list[2]
      print(add_time(time, length, day))
    else:
      print(add_time(time, length))