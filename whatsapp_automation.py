import pywhatkit as kit

number = ''

# syntax: phone number with country code, message, hour and minutes
# pywhatkit.sendwhatmsg('+1xxxxxxxx', 'Message 1', 18, 52)
# What this code means is “Type ‘Message 1’ and send it to contact X at 18:52”
# Here the “True” indicates that we want to close the tab after “X” seconds once the message is delivered. The last argument “2” represents this “X” number of seconds.

kit.sendwhatmsg(number, 'Hi', 15, 29)

