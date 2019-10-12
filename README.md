# Web-Scrapping-from-Beginner-to-Advance

I explain how to use python to send get requests to web Servers and then parse the Response 

e.g : https://en.wikipedia.org/wiki/URL?key=value&life=42#History 

URL
U = Uniform
R = Resource
L = Locator


Scheme :

        Protocol : Https,Http,ftp.....
        Host : en.wikipedia.org
        Port : http=80, https=443
        Path : wiki/URL
        QueryString : key=value&life=42
        Fragment : History ... is used to jump in a section within the webpage

Python 3 comes equipped with a package that simplifies the task of building,loading and Parsing URLs

urllib package : 1)request : used to open URLs
                 2)response : used internally
                 3)error : Contains several error classes for use by the request module
                 4)parse: Variety of functions for breaking up a URL into meaningful pieces like the sceme 
                 5)robotparser : robots.txt files for what permissions are granted to bots and crawlers 
