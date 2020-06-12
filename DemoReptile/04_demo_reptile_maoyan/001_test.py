import requests

r = requests.get('https://maoyan.com/board/4')
print('111: ', type(r))
print('\n222: ', r.status_code)
print('\n333: ', type(r.text))
print('\n444: ', r.text)
print('\n555: ', r.cookies)
