import sys
from behave import given, when, then
from hamcrest import assert_that, equal_to, has_item
sys.path.insert(0, 'bin')
from find import Findapp

@given(u'name of "{directory}" and "{pattern}"')
def step_impl(context, directory, pattern):
	context.findapp = Findapp(directory, pattern)
	assert_that(context.findapp.directory, equal_to(directory))
	assert_that(context.findapp.pattern, equal_to(pattern))

@when(u'I execute definition')
def step_impl(context):
	context.findapp.find_impl()

@then(u'result should contain "{expected_file}" file')
def step_impl(context, expected_file):
	assert_that(context.findapp.result, has_item(expected_file))
