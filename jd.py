# _*_coding:utf-8_*_

#!/usr/bin/

from selenium import webdriver

class JD(object):

    def __init__(self):
        driver = webdriver.Firefox()
        self.driver = driver

    def login(self, username="null", userpwd="null"):
        if (username == 'null' or userpwd == 'null'):
            return

        self.driver.get("https://passport.jd.com/new/login.aspx")
        self.driver.find_element_by_link_text("账户登录").click()
        self.driver.find_element_by_id("loginname").send_keys(username)
        self.driver.find_element_by_id("nloginpwd").send_keys(userpwd)
        self.driver.find_element_by_id("loginsubmit").click()

    def query(self, url):
        self.driver.get(url)

def get_args():
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('--username', dest='username', default='null', help='user name')
    parser.add_argument('--userpwd', dest='userpwd', default='null', help='user password')
    parser.add_argument('--url', dest='url', default='null', help='url')

    return parser.parse_args()

def main():

    args = get_args()

    jd = JD()
    jd.login(args.username, args.userpwd)
    jd.query(args.url)

if __name__ == '__main__':
	main()
