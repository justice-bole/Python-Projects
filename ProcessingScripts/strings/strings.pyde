greeting = 'Hello, World!'
print(greeting)
whatsup = 'What\'s up?'
question = 'Is your name really "World?"'
print(whatsup)
print(question)
all = greeting + ' ' + whatsup + ' ' + question
print(all)
all = '{} {} {}'.format(greeting, whatsup, question)
print(all)
print(len(greeting))

url = 'http://www.nostarch.com'
print(url[:7])
print(url[7:])
print(url[-3:])
print(url[11:-4])

css = url.find('://') #4
scheme = url[:css] #http
dot1 = url.find('.') #10
subdomain = url[css+3:dot1] #www
dot2 = url.find('.', dot1+1) #19
tld = url[dot2:] #com
domain = url[dot1+1:dot2] #nostarch

textString = 'Scheme: {}\nSubdomain: {}\nTopLevelDomain: {}\nDomain: {}'.format(scheme, subdomain, tld, domain)
print(textString)
