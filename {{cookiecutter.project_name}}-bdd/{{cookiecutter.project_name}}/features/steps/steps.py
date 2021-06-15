from behave import given, then, when, step


@given('')
def simpl_step(context):
    context.logger.info('Logging Example')
    pass


@then('')
def simpl_step(context):
    pass


@when('')
def simpl_step(context):
    pass


@step('')
def simpl_step(context):
    pass
