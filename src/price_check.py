from datetime import date
from send_email import send_mail
from crawler import crawl_site_by_name
from data_manager import store_data, init_db, load, unique_vendors
import argparse


def run_price_checker(usr, pwd):
    msg = ""
    for company in unique_vendors():
        try:
            price = crawl_site_by_name(company)
            store_data(company, price)
            msg += '''
            <tr>
            <td>{0}</th>
            <td>{1}</th>
            </tr>
            '''.format(company, price)
        except Exception as e:
            msg += str(e) + "\n"

    today = date.today().isoformat()
    send_mail(usr, pwd, msg, today)


if __name__=='__main__':
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
        elif args.action == "run":
            #assert args.username is not None
            #assert args.password is not None
            run_price_checker(args.username, args.password)
