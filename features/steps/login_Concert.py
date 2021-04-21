from behave import *
from common.read_Properties import ReadConfig

base_Url = ReadConfig.get_application_url()

@given('Open Concert')
def open_concert(context):
    context.helperfunc.open('https://concert.centrals.eu.dev.its-siemens.com/tsc/client/home/')
    context.helperfunc.maximize()


@then(u'Login concert')
def step_impl(context):
    context.value = base_Url
    print(context.value)



@then(u'Verify title of concert')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Verify title of concert')


@then(u'Close the browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Close the browser')