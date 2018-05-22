#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yangxvhao'
__time__ = '18-5-7'

import base64
import urllib.parse
import urllib.request


def test():
    n = 100
    v = [1,  5, 10, 25, 50]
    l = [i == 0 for i in range(n+1)] 
    for i in range(len(v)):
        for j in range(v[i], len(l)):
            l[j] += l[j - v[i]]

    print(l)


def get_token():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=yGDbW8cYPPVr5Csu5gnBX4IH&' \
           'client_secret=cxr9oNAqUxVtG0el480nn3qZecTGKNt1'
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    if content:
        print(content)


access_token = '24.bd1f4817e1d5ce924cc5e2ee071bbc91.2592000.1528278454.282335-11204187'


def get_photo_base64(photo_file):
    f = open(photo_file, 'rb')
    photo_base64 = base64.b64encode(f.read())
    f.close()
    # print(photo_base64)
    return photo_base64


'''
人脸检测与属性分析
'''


def face_test(photo_file):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    photo_url = 'https://cloud-minapp-14591.cloud.ifanrusercontent.com/1fFsEvOSXChaNJmQ.jpg'
    # "{\"image\":\"" + str(get_photo_base64(photo_file)) + "\",\"image_type\":\"FACE_TOKEN\",\"face_field\":\"faceshape,facetype\"}"
    # params = dict(image=get_photo_base64(photo_file), image_type='URL', face_field='age,beauty,expression,faceshape,gender,glasses,race')
    params = dict(image=photo_url, image_type='URL', face_field='age,beauty,expression,faceshape,gender,glasses,race')
    params = urllib.parse.urlencode(params).encode('utf-8')
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request)
    content = response.read()
    if content:
        print(content)


if __name__ == '__main__':
    # test()
    face_test('/home/yangxvhao/图片/webwxgetmsgimg.jpg')
    # get_token()