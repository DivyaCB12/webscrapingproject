import requests
from bs4 import BeautifulSoup

products_to_track = [
    {
        "product_url":"https://www.amazon.in/Samsung-Galaxy-M12-Storage-Processor/dp/B08XGDN3TZ/ref=sr_1_1?crid=1Y4JV9YP59ENG&dchild=1&keywords=mobile&qid=1635750639&sprefix=mobil%2Cspecialty-aps%2C371&sr=8-1",
        "name":"Samsung-Galaxy-M12",
        "target_price":10000
    },
    {
        "product_url":"https://www.amazon.in/dp/B096VDR283/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B096VDR283&pd_rd_w=AuFn7&pf_rd_p=4e9225d2-7473-4eb0-95d5-670190275218&pd_rd_wg=2gNom&pf_rd_r=RDK3QDTBVBE5KEW75HE3&pd_rd_r=0fbc308c-0d7b-4a4d-a659-87960647c47f&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzQ1AyMURCN1EzNUlEJmVuY3J5cHRlZElkPUEwMTA5MTMwSThVQlNWRElYOUJDJmVuY3J5cHRlZEFkSWQ9QTAxODk5ODQyWE5ER1lTUTNVTzNGJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ",
        "name":"Samsung-Galaxy-M32",
        "target_price":15000
    },
    {
        "product_url":"https://www.amazon.in/Samsung-Galaxy-Blue-128GB-Storage/dp/B09CGJK2HG/ref=psdc_1805560031_t1_B096VDR283",
        "name":"Samsung-Galaxy-Blue",
        "target_price":16000
    },
    {
        "product_url":"https://www.amazon.in/Silver-Storage-Additional-Exchange-Offers/dp/B08LRDK8Z5/ref=sr_1_1_sspa?crid=1JZ6BZC087FUG&dchild=1&keywords=mobiles+under+15%2C000%2B&qid=1635752063&s=electronics&sprefix=MOB%2Celectronics%2C665&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFRUkZIWkJBWUVWMEkmZW5jcnlwdGVkSWQ9QTA0ODM1NTEzOUNSWU9MNDlJV0ozJmVuY3J5cHRlZEFkSWQ9QTA1NjAxNjEzS0ZSSDRZQ000SzNLJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ",
        "name":"oppo",
        "target_price":29000
    },
    {
        "product_url":"https://www.amazon.in/dp/B085J1KCGP/ref=sspa_dk_detail_4?psc=1&pd_rd_i=B085J1KCGP&pd_rd_w=W8uGN&pf_rd_p=4e9225d2-7473-4eb0-95d5-670190275218&pd_rd_wg=IvCz2&pf_rd_r=SEYF58C35M4VECE0V4CC&pd_rd_r=2ee97a8f-eaf7-4d9e-a00d-e5080cfe1eb3&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMlZLNzg1TkFTWUVGJmVuY3J5cHRlZElkPUEwNTg1MTg3WU1NWVk0STVMN01TJmVuY3J5cHRlZEFkSWQ9QTAzNzYxMzRIUEdSUDVRRFg3R1cmd2lkZ2V0TmFtZT1zcF9kZXRhaWwmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl",
        "name":"vivo",
        "target_price":35000
    }
]
def give_product_price(URL):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

    }
    page = requests.get(URL,headers = headers)
    soup = BeautifulSoup(page.content,'html.parser')
    product_price = soup.find(id="priceblock_dealprice")

    return product_price.getText()
    print(product_price)
    print(product_price.getText())

result_file = open('my_result_file.txt','w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + " _ " + every_product.get("name"))

        my_product_price_returned = product_price_returned[1:]
        my_product_price_returned = my_product_price_returned.replace(',','')
        my_product_price_returned = int(float(my_product_price_returned))

        print(my_product_price_returned)
        if my_product_price_returned < every_product.get("target_price") :
            print("Available at your required price")
            result_file.write(every_product.get("name") + ' - \t' + 'Available at Target Price ' + ' Current Price - ' + str(my_product_price_returned)+ '\n')

        else :
            print("still at current price")
finally :
    result_file.close()

import requests
