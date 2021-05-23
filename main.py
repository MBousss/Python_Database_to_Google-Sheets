#!/usr/bin/env python

import datetime
import os
import traceback

from configuration import Configuration
from database import DataBase
from sheets import Sheet


def main():
    ''' This program will be able to execute multiple tasks 
        to fetch data and put it in Google Sheets
        
        Task:
            A task is a operation of fetching data from a MySql DataBase
            and uploads it to a Google Sheet
            
        How to make a new Task:
            1: Make a new directory in the 'tasks' directory
            2: Create a 'credentials.json' file
                - Read doc's in 'configuration.py' for layout
            3: Create a 'query.sql' file
    '''
    tasks_dir = "tasks/"

    for task in os.listdir(tasks_dir):
        if os.path.isdir('{}/{}'.format(tasks_dir, task)):
            config = Configuration(task_path=task)
            try:
                # Get data from database
                dbData = DataBase(config=config).getTableData()
                columns = dbData['column_names']
                data = dbData['table_data']

                # Upload data to sheet
                sheet = Sheet(config=config)
                sheet.clear_sheet()
                sheet.upload_data(columns=columns, data=data, date_time=True)
                printMessage("Completed task: " + task)
            except Exception as error:
                printMessage("{} => {}".format(task, error))
                traceback.print_exc()

    return 0


def printMessage(inputMessage):
    message = '[{}] {}'.format(getCurrentDateTimeFormatted(), inputMessage)
    print(message)


def getCurrentDateTimeFormatted():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    main()
