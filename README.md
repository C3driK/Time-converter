# Time-converter
The add_time function takes in a start time, a duration to add, and an optional day of the week. Here's how it works:

First, it converts the start time from 12-hour format to 24-hour format, and then it converts the duration into minutes.
Next, it calculates the new time by adding the start time and the duration.
It also calculates the new period (AM or PM) based on the new hour.
Then, it calculates the number of days later.
If a day is provided, it calculates the new day of the week and formats the output accordingly.
Finally, it returns the new time in the specified format.
The function also handles edge cases such as:

Period change at 12:00
Handling midnight
Formatting the output with or without the day of the week.
This add_time function is useful for adding time to a given start time and can also handle day of the week if provided.
