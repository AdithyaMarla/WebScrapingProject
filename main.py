import requests
from bs4 import BeautifulSoup

products_to_track = [

    {
        "URL":"https://www.nike.com/in/t/air-jordan-1-mid-se-shoes-CQ6f9G/DV1308-104",
        "Price":"12295.00",
        "Target_price":13000.00
    },
    {
        "URL":"https://www.nike.com/in/t/air-jordan-1-mid-shoes-SQf7DM/DQ8426-014",
        "Price":"11495.00",
        "Target_price":10000.00
    },
    {
        "URL":"https://www.nike.com/in/t/air-force-1-07-shoes-WrLlWX/CW2288-111",
        "Price":"7495.00",
        "Target_price":7000.00
    },
    {
        "URL":"https://www.nike.com/in/t/court-vision-low-next-nature-shoes-N2fFHb/DH2987-100",
        "Price":"4995.00",
        "Target_price":4500.00
    },
    {
        "URL":"https://www.nike.com/in/t/nikecourt-royale-2-next-nature-shoes-RRcr20/DH3160-001",
        "Price":"3995.00",
        "Target_price":4000.00
    }
]

def give_product_name(URL):
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    product_name = soup.find(id="pdp_product_title")
    return product_name.getText()

result_file = open('my_result_file.txt','w')

try:
    for every_product in products_to_track:
        Product_name = give_product_name(every_product.get("URL"))
        print(Product_name + "  -  " + every_product.get("Price"))


        if float(every_product.get("Price"))<=every_product.get("Target_price"):
            print("Less than target price")
            result_file.write(Product_name+' - '+'Less than target price.\n'+'Previous price-'+ every_product.get("Price")+'\n')
        else:
            print("Still at current price")

finally:
    result_file.close()
