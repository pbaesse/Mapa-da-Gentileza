from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/usr/lib/firefox/firefox')

def after_scenario(context, scenario):
    save_to_file(context, scenario)


def before_feature(context, feature):
    context.browser = webdriver.Firefox(firefox_binary=binary)


def after_feature(context, feature):
    context.browser.quit()


def save_to_file(context, scenario):
    with open('result_tests_scenarios.txt', 'a') as file:
        file.write("Scenario: {} \n \t".format(context.scenario.name))
        file.write("Feature to which it belongs: {} \n \t".format(context.scenario.feature))
        file.write("Duration: {} s \n \t".format(context.scenario.duration))
        file.write("Filename: {} \n \t".format(context.scenario.filename))
        file.write("Status: {} \n\n".format(str(context.scenario.status)))
        file.write("------------------------------------------- \n \n")