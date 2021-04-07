import unittest
from selenium import webdriver
from time import sleep
import csv
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# 以utf-8-sig的编码格式打开文件，-sig加上避免转义，UTF-8 with BOM即utf-8-sig
bid_info=csv.DictReader(open('template_item.csv',encoding='utf-8-sig'))

#取表格中的所有数据
list_data=[]
for lines in bid_info:
    if bid_info.line_num==1:
        continue
    else:
        list_data.append(lines)
row_num=len(list_data)

#取表格中item_template_id的所有值
list_template_id=[]
i=0
while i<row_num:
    value=list_data[i]['item_template_id']
    list_template_id.append(value)
    i+=1

num=0
while num<row_num:

    class MailSending(unittest.TestCase):
        def setUp(self):
            self.driver=webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.base_url="http://admin.qmwg.xpjplayer.com/Admin/Default.html"

        def test_addmail(self):
            driver=self.driver
            driver.get(self.base_url)
            driver.maximize_window()#设置窗口最大化
            # driver.set_window_size(1920,1080)#设置窗口分辨率
            driver.find_element_by_name('Account').send_keys('admin1')
            driver.find_element_by_name('Password').send_keys('cd@snqp@123')
            sleep(1)
            driver.find_element_by_css_selector("button[data-tap=Submit]").click()
            sleep(1)
            driver.find_element_by_css_selector("item[data-value=Email]").click()
            sleep(3)
            # driver.find_element_by_css_selector("div[data-value=Append]").send_keys(Keys.ENTER)
            element=driver.find_element_by_xpath("//*[text()='添加']").click()
            driver.ActionChains(driver).move_to_element(element).click(element).perform()#鼠标悬停方法
            # driver.execute_script('arguments[0].click();',element)
            # js='document.getElementByCssSelector("div[data-value=Append]"]).click()'
            # driver.execute_script(js)
            sleep(1)
            driver.find_element_by_css_selector("input[data-name=Number]").send_keys('10015')
            sleep(1)
            driver.find_element_by_css_selector("input[data-name=Title]").send_keys('标题')
            sleep(1)
            driver.find_element_by_css_selector("input[data-name=Content]").send_keys('内容')
            sleep(1)
            driver.find_element_by_css_selector("input[data-name=ItemInfo]").send_keys(list_template_id[num]*10000)
            num+=1
            sleep(1)
            driver.find_element_by_css_selector("input[data-name=SendTime]").send_keys(time.strftime("%Y/%m/%d %H:%M:%S",time.localtime()))
            sleep(1)
            driver.find_element_by_css_selector("button[data-name=Positive]").click()





    def test_something(self):
        self.assertEqual(True, False)


    if __name__ == '__main__':
        unittest.main()

