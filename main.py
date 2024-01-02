def add_time(start, duration, day=None):
  
  # Convert start time to 24-hour format
  start_time, period = start.split()
  start_hour, start_min = map(int, start_time.split(':'))
  if period == 'PM':
      start_hour += 12
  # Convert duration to minutes
  duration_hour, duration_min = map(int, duration.split(':'))
  total_min = start_hour * 60 + start_min + duration_hour * 60 + duration_min
  # Calculate new time
  new_hour = total_min // 60 % 24
  new_min = total_min % 60
  new_period = 'AM' if new_hour < 12 else 'PM'
  if new_hour > 12:
      new_hour -= 12
  elif new_hour == 0:
      new_hour = 12
  # Calculate days later
  days_later = total_min // (24 * 60)
  if day:
      # Calculate new day of the week
      days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
      day_index = days.index(day.lower().capitalize())
      new_day_index = (day_index + days_later) % 7
      new_day = days[new_day_index]
      # Format output with day of the week
      if days_later == 0:
          if new_period == period:
              return f'{new_hour}:{new_min:02d} {period}, {day}'
          else:
              return f'{new_hour}:{new_min:02d} {new_period}, {day}'
      elif days_later == 1:
          return f'{new_hour}:{new_min:02d} {new_period}, {new_day} (next day)'
      else:
          return f'{new_hour}:{new_min:02d} {new_period}, {new_day} ({days_later} days later)'
  else:
      # Format output without day of the week
      if days_later == 0:
          if new_period == period:
              return f'{new_hour}:{new_min:02d} {period}'
          else:
              return f'{new_hour}:{new_min:02d} {new_period}'
      elif days_later == 1:
          return f'{new_hour}:{new_min:02d} {new_period} (next day)'
      else:
          return f'{new_hour}:{new_min:02d} {new_period} ({days_later} days later)'
