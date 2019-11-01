#!/usr/bin/python3
# -*- coding:utf-8 -*-

import drawingDisplay
import json
def main():
    with open('calendar.json', 'r', encoding='utf-8') as fh: #открываем файл на чтение
        data_dict = json.load(fh) #загружаем из файла данные в словарь data

    values = data_dict.items()
    for k, v in values:
        roomSchedule = v
        title = k

    print(title)
    print(roomSchedule)

    print('Start Creat display')
    display = drawingDisplay.DrawingDisplay(title, '%d/%m/%Y %H:%M')

  #  roomSchedule = [{"StartTime":"01/29/2019 10:00:00","EndTime":"01/29/2019 13:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое 1","Category":"","MeetingExternalLink":None},{"StartTime":"01/29/2019 13:00:00","EndTime":"01/29/2019 14:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое 2","Category":"","MeetingExternalLink":None},{"StartTime":"01/29/2019 14:00:00","EndTime":"01/29/2019 15:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое 3","Category":"","MeetingExternalLink":None},{"StartTime":"01/29/2019 14:00:00","EndTime":"01/29/2019 15:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое 3","Category":"","MeetingExternalLink":None},{"StartTime":"01/29/2019 14:00:00","EndTime":"01/29/2019 15:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое 3","Category":"","MeetingExternalLink":None}]
# # roomSchedule = [{"StartTime":"01/29/2019 10:00:00","EndTime":"01/29/2019 13:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое 1","Category":"","MeetingExternalLink":None}]
# # roomSchedule = [{"StartTime":"01/29/2019 10:00:00","EndTime":"01/29/2019 13:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое мероприятие","Category":"","MeetingExternalLink":None},{"StartTime":"01/29/2019 13:00:00","EndTime":"01/29/2019 14:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое 2","Category":"","MeetingExternalLink":None},{"StartTime":"01/29/2019 14:00:00","EndTime":"01/29/2019 15:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое 3","Category":"","MeetingExternalLink":None},{"StartTime":"01/29/2019 14:00:00","EndTime":"01/29/2019 15:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое 3","Category":"","MeetingExternalLink":None},{"StartTime":"01/29/2019 14:00:00","EndTime":"01/29/2019 15:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое 3","Category":"","MeetingExternalLink":None}]
# # roomSchedule = [{"StartTime":"01/29/2019 10:00:00","EndTime":"01/29/2019 13:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое мероприятие","Category":"","MeetingExternalLink":None},{"StartTime":"01/29/2019 13:00:00","EndTime":"01/29/2019 14:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое мероприятие 2","Category":"","MeetingExternalLink":None},{"StartTime":"01/29/2019 14:00:00","EndTime":"01/29/2019 15:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое 3","Category":"","MeetingExternalLink":None},{"StartTime":"01/29/2019 14:00:00","EndTime":"01/29/2019 15:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое 3","Category":"","MeetingExternalLink":None},{"StartTime":"01/29/2019 14:00:00","EndTime":"01/29/2019 15:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое 3","Category":"","MeetingExternalLink":None}]
# # roomSchedule = [{"StartTime":"01/29/2019 10:00:00","EndTime":"01/29/2019 13:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое мероприятие","Category":"","MeetingExternalLink":None}]
   # roomSchedule = [{"StartTime":"01/02/2019 16:00","EndTime":"01/02/2019 19:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое мероприятие","Category":"","MeetingExternalLink":None},{"StartTime":"01/02/2019 19:00","EndTime":"01/02/2019 20:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое 2","Category":"","MeetingExternalLink":None},{"StartTime":"01/02/2019 20:00","EndTime":"01/02/2019 21:30","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое 3","Category":"","MeetingExternalLink":None}]
# # roomSchedule = []

    display.drawDisplay(roomSchedule)

if __name__ == "__main__":
    main()


#display.drawTwoLinesDisplay()

# {
#     'type': 'object',
#     'properties': {
#         'RoomId': {
#             'type': 'string'
#         },
#         'Schedule': {
#             'type': 'array',
#             'items': {}
#         }
#     },
#     'required': [
#         'RoomId',
#         'Schedule'
#     ]
# }

# 29/01/19 12:47:50 sucessfully handling ScheduleOutput message {"RoomId":"Conf Room MTC Msc Alexander Garden_26","Schedule":[{"StartTime":"01/29/2019 10:00:00","EndTime":"01/29/2019 13:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое мероприятие","Category":"","MeetingExternalLink":null}]}
# 29/01/19 12:59:49 sucessfully handling ScheduleOutput message {"RoomId":"Conf Room MTC Msc Alexander Garden_26","Schedule":[{"StartTime":"01/29/2019 10:00:00","EndTime":"01/29/2019 13:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое мероприятие","Category":"","MeetingExternalLink":null},{"StartTime":"01/29/2019 13:00:00","EndTime":"01/29/2019 14:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое 2","Category":"","MeetingExternalLink":null},{"StartTime":"01/29/2019 14:00:00","EndTime":"01/29/2019 15:00:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое 3","Category":"","MeetingExternalLink":null}]}
# 01/02/19 12:26:53 sucessfully handling ScheduleOutput message as {"RoomId":"Conf Room MTC Msc Alexander Garden_26","Schedule":[{"StartTime":"01/02/2019 16:00","EndTime":"01/02/2019 19:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое мероприятие","Category":"","MeetingExternalLink":null},{"StartTime":"01/02/2019 19:00","EndTime":"01/02/2019 20:00","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое 2","Category":"","MeetingExternalLink":null},{"StartTime":"01/02/2019 20:00","EndTime":"01/02/2019 21:30","Location":"Conf Room MTC Msc Alexander Garden_26","Title":"MTC Moscow (Russia) Тестовое 3","Category":"","MeetingExternalLink":null}]}
