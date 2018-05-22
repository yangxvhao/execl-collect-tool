#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yangxvhao'
__time__ = '18-4-9'

import xlrd
import xlwt
import os

result_title = []
for i in range(0, 50):
    result_title.append(0)

result_cell = ['工资月份', '工号', '姓名', '出勤小时', '应付工资', '应发工资']


def read_execl(file_name):
    data = xlrd.open_workbook(file_name)
    sheets = data.sheets()

    months = set()
    persons = []

    for sheet in sheets:
        rows = sheet.nrows
        for i in range(rows):
            cells = sheet.row_values(i)
            # 表头结束的行数
            if i <= 3:
                for j in range(len(cells)):
                    if cells[j].replace(" ", "") in result_cell:
                        result_title[j] = cells[j].replace(" ", "")
            if i <= 3:
                continue
            person_info = []
            try:
                for result in range(0, len(result_title)):
                    sheet_data = sheet.cell(i, result).value
                    if sheet_data != "小计" or sheet_data != "合计":
                        person_info.append(sheet.cell(i, result).value)
                    if result_title[result] == "工资月份":
                        months.add(sheet_data)
                # month = sheet.cell(i, result_title.index(result_cell[0])).value
                # job_number = sheet.cell(i, result_title.index(result_cell[1])).value
                # name = sheet.cell(i, result_title.index(result_cell[2])).value
                # work_time = sheet.cell(i, result_title.index(result_cell[3])).value
                # wage_payable = sheet.cell(i, result_title.index(result_cell[4])).value
                # real_payable = sheet.cell(i, result_title.index(result_cell[5])).value
            except Exception as e:
                print('工作表' + str(sheet.name) + ',列异常:' + str(e))
                return persons, months
            # if name == '小计' or name == '合计':
            #     continue
            # months.add(month)
            # person_info.append(month)
            # person_info.append(job_number)
            # person_info.append(name)
            # person_info.append(work_time)
            # person_info.append(wage_payable)
            # person_info.append(real_payable)

            persons.append(person_info)
    print(months)
    return persons, months


def split(persons, months):
    result = []
    for month in months:
        person_list = []
        for person in persons:
            if person[0] == month:
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

        for i in range(1, len(result_cell)):
            sheet.write(0, i - 1, result_cell[i])

        person_list = result[ii]
        for i in range(0, len(person_list)):
            for j in range(1, len(person_list[i])):
                sheet.write(i + 1, j - 1, person_list[i][j])

    data.save(write_name)


def read_file_of_dir(dir):
    files = os.listdir(dir)
    for file in files:
        if file.endswith('xls') or file.endswith('xlsx'):
            read_file = os.path.join(dir, file)
            write_file_name = file.split(".xls")[0] + "汇总.xls"
            result_path = os.path.join(dir, 'result')
            if not os.path.exists(result_path):
                os.mkdir(result_path)
            write_file = os.path.join(result_path, write_file_name)
            write_execl(read_file, write_file)


if __name__ == '__main__':
    read_dir = "/home/yangxvhao/work/document/execl-collect"
    read_file_of_dir(read_dir)