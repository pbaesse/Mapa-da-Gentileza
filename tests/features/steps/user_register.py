from behave import given, when, then

data = {
    'username' : 'username',
    'email' : 'email',
    'password' : 'password',
    'SignUp' : 'SignUp'
}


@given('that the user is on the page "{page}"')
def access_page(context, page):
    context.browser.get(page)


@when('insert the "{field}" "{value}"')
def insert_values_on_fields(context, field, value):
    context.browser.find_element_by_id(data[field]).send_keys(value)


@then('click the button "{btn}"')
def click(context, btn):
    context.browser.find_element_by_id(data[btn]).click()


@then('the message should be displayed')
def read_msg(context):
    page_h1 = context.browser.find_element_by_id('msg').text
    assert context.text == page_h1.text, '''
    {} != {}''' .format(page_h1, context.text) 
