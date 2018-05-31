
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

def first():
    '''
    打开页面，进行搜索
    browser = webdriver.Chrome()
    browser = webdriver.Firefox()
    browser = webdriver.Edge()
    browser = webdriver.PhantomJS()
    browser = webdriver.Safari()
    节点操作：输入内容，清空输入框
    input.send_keys('iPhone') 
    input.clear()
    '''
    browser = webdriver.Chrome()
    try:
        browser.get('https://www.baidu.com')
        input = browser.find_element_by_id('kw') # 属性id为kw的数据
        input.send_keys('Python')
        input.send_keys(Keys.ENTER)
        # wait = WebDriverWait(browser, 10)
        # wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
        print(browser.current_url)
        print(browser.get_cookies())
        print(browser.page_source)
    finally:
        # browser.close()
        print("结束")


def second():
    '''
    查找节点方式 获取节点：属性，文本值，id、位置、标签名和大小
    find_element_by_id
    find_element_by_name
    find_element_by_xpath
    find_element_by_link_text
    find_element_by_partial_link_text
    find_element_by_tag_name
    find_element_by_class_name
    find_element_by_css_selector
    多个节点查找
    element多了一个s
    eg:lis = browser.find_elements_by_css_selector('.service-bd li')
    '''
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    input_first = browser.find_element_by_id('q')
    input_second = browser.find_element_by_css_selector('#q')
    input_third = browser.find_element_by_xpath('//*[@id="q"]')
    print(input_first, input_second, input_third)
    print(input_first.get_attribute('class')) # 属性内容
    print(input_first.text) # 文本内容
    print(input_first.id) # id内容
    print(input_first.location) # 位置内容
    print(input_first.tag_name) # 标签名
    print(input_first.size) # 大小
    # browser.close()
    import time
    time.sleep(7)
    print("结束")


def third():
    '''
    http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains
    鼠标操作：单击、双击、点击鼠标右键、拖拽等等
    处理这类事件——ActionChains
    click(on_element=None) ——单击鼠标左键
    click_and_hold(on_element=None) ——点击鼠标左键，不松开
    context_click(on_element=None) ——点击鼠标右键
    double_click(on_element=None) ——双击鼠标左键
    drag_and_drop(source, target) ——拖拽到某个元素然后松开
    drag_and_drop_by_offset(source, xoffset, yoffset) ——拖拽到某个坐标然后松开
    key_down(value, element=None) ——按下某个键盘上的键
    key_up(value, element=None) ——松开某个键
    move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标
    move_to_element(to_element) ——鼠标移动到某个元素
    move_to_element_with_offset(to_element, xoffset, yoffset) ——移动到距某个元素（左上角坐标）多少距离的位置
    perform() ——执行链中的所有动作
    release(on_element=None) ——在某个元素位置松开鼠标左键
    send_keys(*keys_to_send) ——发送某个键到当前焦点的元素
    send_keys_to_element(element, *keys_to_send) ——发送某个键到指定元素
    '''
    browser = webdriver.Chrome()
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to.frame('iframeResult') # 转换操作界面
    source = browser.find_element_by_css_selector('#draggable')
    target = browser.find_element_by_css_selector('#droppable')
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    actions.perform() # 执行
    '''
    执行 JavaScript脚本
    JavaScript
    '''
    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.execute_script('alert("To Bottom")')
    import time
    time.sleep(7)


'''
隐式等待
如果Selenium没有在DOM中找到节点，将继续等待，超出设定时间后，则抛出找不到节点的异常。
browser.implicitly_wait(10)
显式等待
规定了一个固定时间，查找的节点,而页面的加载时间会受到网络条件的影响。
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)
'''

def fourth():
    '''
    浏览器操作
    后退，前进
    Cookies进行操作，例如获取、添加、删除Cookies
    切换窗口
    '''
    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com/')
    browser.get('https://www.taobao.com/')
    browser.back() # 后退
    browser.forward() # 前进

    print(browser.get_cookies())
    browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
    browser.delete_all_cookies()

    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[1])
    browser.switch_to_window(browser.window_handles[0])

if __name__  == "__main__":
    # first()
    # second()
    # third()
    fourth()