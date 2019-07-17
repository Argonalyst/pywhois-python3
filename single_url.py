import pywhois

w = pywhois.whois('google.com')
print(w.emails)
print(w)