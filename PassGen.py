# Imports
import secrets
import string

# Define variables.
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
white_spaces = string.whitespace

pattern = letters + digits + special_chars + white_spaces

# Set password lenght.
password_length = 24

# Generate a password string.
password = ''
for i in range(password_length):
  password += ''.join(secrets.choice(pattern))
print(password)

# Generate password with constraints.
while True:
  password = ''
  for i in range(password_length):
    password += ''.join(secrets.choice(pattern))

  if (any(char in special_chars for char in password) and 
      sum(char in digits for char in password)>=2):
          break
print(password)
