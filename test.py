site = 'http://youtube.com/watch?v=giYeaKsXnsI'
http://youtube.com/embed/giYeaKsXnsI


def modyfi(site):
   if site.startswith('http://'):
        url = site.replace('http://', 'https://', 1)
        return url


print(modyfi(site))