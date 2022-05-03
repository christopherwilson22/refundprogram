days_bought =int(input('How many days ago did you buy? ')) 
itembroken = input('Did the item break on its own [y/n]? ') 
use_of_item = input('Did you use the item [y/n] ') 

if itembroken == 'y' and days_bought <=10 and use_of_item == 'n': 
    print('You can get a refund') 
else:
    print('You can not get a refund')