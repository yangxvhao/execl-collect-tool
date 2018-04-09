#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yangxvhao'
__time__ = '18-4-9'

import xlrd
import xlwt

title = ['姓名', '出勤时数', '全勤奖']


def read_execl(file_name):

    data = xlrd.open_workbook(file_name)
    sheets = data.sheets()

    months = set()
    persons = []
    rows_info = []

    for sheet in sheets:
        rows = sheet.nrows
        for i in range(rows):

            if i < 3:
                continue
            if i == 3:
                rows_info = sheet.row_values(i)
                continue
            person_info = []

            month = sheet.cell(i, 1).value
            name = sheet.cell(i, 2).value
            work_time = sheet.cell(i, 3).value
            if '全勤奖' in rows_info:
                pay = sheet.cell(i, 5).value
            else:
                pay = 0

            if name == '小计' or name == '合计':
                continue
            months.add(month)
            person_info.append(month)
            person_info.append(name)
            person_info.append(work_time)
            person_info.append(pay)

            persons.append(person_info)
    print(months)
    return persons, months


def write_execl(file_name):
    data = xlwt.Workbook()
    person_list, months = read_execl(file_name)

    for month in months:
        sheet = data.add_sheet(str(month) + '月')

        for i in range(0, len(title)):
            sheet.write(0, i, title[i])

        for i in range(1, len(person_list)):
            for j in range(1, len(person_list[i])):
                if person_list[i][0] == months:
                    sheet.write(i, j, person_list[i][j])

    data.save(file_name)


if __name__ == '__main__':
    write_execl("/home/yangxvhao/work/document/Book2.xlsx")