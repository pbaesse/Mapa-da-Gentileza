from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/usr/lib/firefox/firefox')

def after_scenario(context, scenario):
    print("Testando o metodo after_scenario")
    print(context.scenario.name)
    print(context.scenario.feature)


def before_feature(context, feature):
    context.browser = webdriver.Firefox(firefox_binary=binary)


def after_feature(context, feature):
    context.browser.quit()