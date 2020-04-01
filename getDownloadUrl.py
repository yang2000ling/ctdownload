from selenium import webdriver
import myscrapy
import time
import csv


def GetDownloadUrl(csvPath, driverPath):
    list1 = []
    list2 = myscrapy.csv2list(csvPath)
    driver = webdriver.Chrome(executable_path=driverPath)
    print(list2[0][0])
    driver.get(list2[0][0])
    a = input("登陆账号后在控制台按任意键继续...")
    for i in list2:
        print(i)
        driver.get(i[0])
        while 1:
            try:
                n = driver.find_element_by_class_name('btn.btn-outline-secondary.fs-1.mt-3').get_attribute('href')
                if len(n) >= 100:
                    print(i[1] + '\nlink: ' + n)
                    list1.append([i[1], n])
                    myscrapy.write_log(i[1] + '\nlink: ' + n)
                break
            except Exception as error:
                time.sleep(1)
                myscrapy.write_log('error:'+str(error))
                print(error)
                continue
    myscrapy.printlist(list1)
    with open('finish.csv', 'w+', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for i in list1:
            writer.writerow(i)


if __name__ == "__main__":
    driverPath = 'D:\\webdriver\\chromedriver.exe'
    csvPath = 'file\\wii1.csv'
    GetDownloadUrl(csvPath,driverPath)
