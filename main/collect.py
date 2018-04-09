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


def split(persons, months):
    result = []
    for month in months:
        person_list = []
        for person in persons:
            if person[0] == month :
                person_list.append(person)
        result.append(person_list)

    return result


def write_execl(read_name, write_name):
    # source_execl = xlrd.open_workbook(read_name)
    # data = copy(source_execl)
    data = xlwt.Workbook()
    person_list, months = read_execl(read_name)

    result = split(person_list, months)

    for ii in range(0, len(result)):
        sheet = data.add_sheet(str(result[ii][0][0]) + '月', cell_overwrite_ok=True)

        for i in range(0, len(title)):
            sheet.write(0, i, title[i])

        person_list = result[ii]
        for i in range(0, len(person_list)):
            for j in range(1, len(person_list[i])):
                sheet.write(i + 1, j - 1, person_list[i][j])

    data.save(write_name)


if __name__ == '__main__':
    read_name = "/home/yangxvhao/work/document/execl-collect/Book1.xlsx"
    write_name = "/home/yangxvhao/work/document/execl-collect/Book2.xlsx"
    write_execl(read_name, write_name)