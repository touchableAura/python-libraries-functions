import requests

thelist = ['apple_juice.jpg', 'apple_pressings.jpg', 'dumplings.jpg', 'lemon_juice.jpg', 'bad_fruit.jpg']
for x in thelist:
    website = requests.get("https://juice-shop.herokuapp.com/assets/images/products/" + x)

    if(website.status_code == 200):
        with open(x, 'wb') as pic:
            pic.write(website.content)



### instructions ###
# run the file in command prompt 
# expect the images from thelist to start appearing 
# (in the same folder this file is located)

### explination ###
# the program scrapes the page from the get request 
# the foor loop checks the page for each string in the list
# if it's there proceed to if statement
# 
