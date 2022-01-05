from bs4 import BeautifulSoup
import requests
import time
import smtplib
import ssl
from email.mime.text import MIMEText as MT
from email.mime.multipart import MIMEMultipart as MM

def get_crypto_price(coin):
    #Get the URL
    url = "https://www.google.com/search?q=" + coin + "+price"

    #make a request to the website
    HTML = requests.get(url, verify=True)

    #parse the HTML
    soup = BeautifulSoup(HTML.text, 'html.parser')

    #find the current price
    text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text

    #return the text
    return text

# store user info
sender = 'hostcybermail@gmail.com'
# receiver = 'kolianick@hotmail.com'
receiver = 'hostcybermail@gmail.com'
sender_password = 'Kalashnikov69'


# unction to email
def send_email(sender, receiver, sender_password, price_text):
    # create MIMEMultipart Object
    msg = MM()
    msg['Subject'] = "New Crypto Price Alert !"
    msg['From'] = sender
    msg['To'] = receiver
    coin = 'Bitcoin'
    # create the HTML for the message
    HTML = """
        <html>
            <body>
                <h1>New Crypto Price Alert! </h1>
                <h2> 
                </h2> 
            </body>
        </html>
        """

    # create a HTML MIMEText Object
    MTObj = MT(HTML, "html")
    # attach the MIMEText Object
    msg.attach(MTObj)

    # create the secure socket layer (SSL) context object
    SSL_context = ssl.create_default_context()
    # create the secure Simple Mail Transfer Protocol (SMTP) connection
    server = smtplib.SMTP_SSL(host="smtp.gmail.com", port=465, context=SSL_context)
    # login to the email
    server.login(sender, sender_password)
    # send the email
    server.sendmail(sender, receiver, msg.as_string())


# function to send the alert
def send_alert():
    last_price = -1
    # create an infinite loop to continuously send/show price
    while True:
        # choose crypto
        coin = 'etherum'
        # get price of crypto
        price = get_crypto_price(coin)
        # check if the price has changed
        if price != last_price:
            print(coin.capitalize()+' price: ', price)
            price_text = coin.capitalize() + ' is ' + price
            send_email(sender, receiver, sender_password, price_text)
            last_price = price  # Update the last price
            time.sleep(3)


send_alert()
