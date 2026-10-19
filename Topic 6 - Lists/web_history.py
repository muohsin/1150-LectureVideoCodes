
# Create an empty list to store the websites visited.
history = []

# Add the websites the user has visited to the history.
history.append('www.google.com')
history.append('www.minneapolis.edu')
history.append('www.stackoverflow.com')

# Display the complete browsing history.
print(history)

# Pressing the back button removes and returns the most recent website.
print(history.pop(), history)

# Go back one more website and display its address.
print(history.pop(), history)

# Go back to the first website and display its address.
print(history.pop(), history)

# Display the history after all websites have been removed.
print(history)
