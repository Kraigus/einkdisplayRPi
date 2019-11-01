from exchangelib import DELEGATE, IMPERSONATION, Account, Credentials, \
    EWSDateTime, EWSTimeZone, Configuration, NTLM, CalendarItem, Message, \
    Mailbox, Attendee, Q
from exchangelib.folders import Calendar

import configparser
import html2text
import datetime
import os
import json
import operator
import temp
import time
import schedule

json_dict = {}
engagement_list = []

def main():
    global engagement_list
    config_file_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'exchange.cfg')

    config = configparser.ConfigParser()
    config.read(config_file_path)

    email = config.get('Settings', 'email')
    try:
        server_url = config.get('Settings', 'server_url')
    except configparser.NoOptionError:
        server_url = None
    password = config.get('Settings', 'password')
    sync_days = int(config.get('Settings', 'sync_days'))
    # org_file_path = config.get('Settings', 'org_file')
    tz_string = config.get('Settings', 'timezone_string')
    sslverify = config.getboolean('Settings', 'verify_ssl')

    tz = EWSTimeZone.timezone(tz_string)

    credentials = Credentials(username=email, password=password)

    if server_url is None:
        account = Account(
            primary_smtp_address=email,
            credentials=credentials,
            autodiscover=True,
            access_type=DELEGATE)
    else:
        server = Configuration(server=server_url, credentials=credentials, verify_ssl=sslverify)
        account = Account(
            primary_smtp_address=email,
            config=server,
            autodiscover=False,
            access_type=DELEGATE)

    now = datetime.datetime.now()
    end = datetime.datetime.replace(now ,hour=23,minute=59,second=59)

    items = account.calendar.filter(
        start__lt=tz.localize(EWSDateTime(end.year, end.month, end.day, end.hour, end.minute)),
        end__gt=tz.localize(EWSDateTime(now.year, now.month, now.day, now.hour, now.minute)), )

    text = []

    json_dict = {email : None}

    for item in items:
        text.append(get_item_text(item, tz))
    text = sorted(text, key=operator.itemgetter('StartTime'))
#   text = sorted(text, key=operator.itemgetter('date'))
    if text[:3] == engagement_list[:3] and bool(text) is not False:
        # print("nothing new")
        return 0
    else:
        # print("printing")
        engagement_list = text.copy()
        json_dict[email] = engagement_list
        with open('calendar.json', "w", encoding="utf-8") as file:
            json.dump(json_dict, file, ensure_ascii=False, indent=2)
        temp.main()


def get_item_date(item, tz):
    date = get_org_date(item.start.astimezone(tz))
    date_dict = {date : None}
    return date_dict


def get_item_text(item, tz):
    meet_dict = {}
    attendee_list = []
    start_date = item.start.astimezone(tz)
    # meet_dict.update({'date' : get_org_date(start_date)})
    # meet_dict.update({'Title': item.subject})

    start_date_text = get_org_time(start_date)
    end_date = item.end.astimezone(tz)
    if (end_date.hour == 0 and end_date.minute == 0):
        end_date = end_date - datetime.timedelta(minutes=1)
    end_date_text = get_org_time(end_date)
    meet_dict.update({'StartTime' : start_date_text})
    meet_dict.update({'EndTime' : end_date_text})

    if item.location is not None:
        meet_dict.update({'Location' : item.location})
    else:
        meet_dict.update({'Location' : None})
    meet_dict.update({'Title': item.subject})

    if item.required_attendees is not None or item.optional_attendees is not None:
        for person in item.required_attendees:
            attendee_list.append(str(person.mailbox.name))
        for person in item.optional_attendees:
            attendee_list.append(str(person.mailbox.name))
#        meet_dict.update({'Attendees' : attendee_list})
    else:
        pass
#        meet_dict.update({'Attendees' : None})

    if item.body is not None:
        meet_dict.update({'Category': html2text.html2text(item.body).replace('\n\n', '\n').replace('\n','')})
    else:
        meet_dict.update({'Category' : None})
    meet_dict.update({'MeetingExternalLink':None})
    return meet_dict

def get_org_date(date):
    return date.strftime('%d/%m/%Y')

def get_org_time(date):
    return date.strftime('%d/%m/%Y %H:%M')

schedule.every(1).minutes.do(main)
schedule.every().hour.at(":00").do(main)
schedule.every(1).minutes.do(main)
schedule.every().hour.at(":30").do(main)



if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
    # main()


