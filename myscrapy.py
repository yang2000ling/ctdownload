import time
import csv
import requests


def sleep(sleep_time):
    """延时函数（单位：秒）"""
    time.sleep(sleep_time)
    print('sleep:' + str(sleep_time) + 's')


def get_source(url, my_data=None, is_ios_header=0, time_out=15, cookie=None):
    """获取url的源代码,返回页面源代码"""
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"}
    ios_header = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"}
    if is_ios_header == 0:
        my_header = header
    else:
        my_header = ios_header
    # print('get_source:',url,'\nparams:',my_data)
    r = requests.get(url, headers=my_header, params=my_data, timeout=time_out, cookies=cookie)
    return r


def write_log(str_log, file_name='out_log.txt'):
    """str_log写入信息,file_name为日志文件名"""
    str_time2s = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
    f = open(file_name, 'a', encoding='utf-8')
    f.write(str_time2s + " :" + str(str_log) + '\n')
    f.close()


def csv2list(csvfile):
    with open(csvfile, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        list1 = []
        for i in reader:
            list1.append(i)
        return list1


def printlist(list):
    counter = 0
    for i in list:
        print(str(counter)+': '+ str(i))
        counter = counter +1
