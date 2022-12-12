import webbrowser as web

def webAutomate():
    chrome_path = 'enter the chrome path'
    # urls to be automated
    URLS = (
         'stackoverflow.com',
         'github.com',
         'gmail.com',
         'youtube.com',
         'google.com'
    )
    
    #looping through the urls and open them one by one
    for url in URLS:
        web.get(chrome_path.open(url))
        