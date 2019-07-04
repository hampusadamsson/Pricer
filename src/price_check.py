from datetime import date
from send_email import send_mail
from crawler import crawl_site_by_name
from data_manager import store_data, init_db, load, unique_vendors, get_vendor_item_price
import argparse


def crawl():
    for company in unique_vendors():
        try:
            price = crawl_site_by_name(company)
            print(company, price)
            store_data(company, price)
        except Exception as e:
            print(str(e))


def get_todays_prices():
    today = date.today().isoformat()
    msg = ""
    for vendor in unique_vendors():
        res = get_vendor_item_price(today, vendor)
        price = str(res[0][0])
        msg += '''
        <tr>
        <td>{0}</th>
        <td>{1}</th>
        </tr>
        '''.format(price, vendor)
    return msg


def email_todays_prices(usr, pwd):
    today = date.today().isoformat()
    msg = get_todays_prices()
    send_mail(usr, pwd, msg, today)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="action")
    parser.add_argument("-username", help="Username for email")
    parser.add_argument("-password", help="Password for email")
    args = parser.parse_args()

    if args.action == "init":
        init_db()
    elif args.action == "history":
        print(load())
    elif args.action == "vendors":
        print(unique_vendors())
    elif args.action == "today":
        print(get_todays_prices())
    elif args.action == "crawl":
        crawl()
    elif args.action == "email":
        email_todays_prices(args.username, args.password)
