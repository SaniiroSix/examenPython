import urllib.request
page = input("Please enter a webpage url: ")
page = urllib.request.urlopen(page)
print(page.read())