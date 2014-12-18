Python BDD Example
=========

This is python behavior driven development example for unix **find** command.

**find** command is not fully featured. Purpose is to demonstrate BDD.

We are using python and behave to drive the BDD.
Assuming that python, behave, pyhamcrest are already installed.

Directory Structure is as follows

```
# tree
.
|-- bin
|   `-- find.py
|-- features
|   `-- findapp.feature
|-- README.md
`-- steps
    `-- findapp_steps.py
```


Create a /features/findapp.feature file. I'm not going through details of .feature file.

``` Cucumber
Feature: Implementing unix find command
        Scenario Outline: unix find command
                Given name of "<directory>" and "<pattern>"
                When I execute definition
                Then result should contain "<expected_file>" file

                Examples:
                        | directory | pattern | expected_file |
                        | .         | .*.py   | ./bin/find.py |
                        | /etc      | .*.bash | /etc/bash.bashrc |
```


"features" and "steps" directories should exists before running 'behave' command.
Run 'behave' command
```bash
#behave
```


After running 'behave' command, we get step definitions which we can safely copy and put it in our "steps/findapp_steps.py" file

```python
@given(u'name of "." and ".*.py"')
def step_impl(context):
    assert False

@when(u'I execute definition')
def step_impl(context):
    assert False

@then(u'result should contain "./bin/find.py" file')
def step_impl(context):
    assert False
```


Now modify your step definition file to pass your first step

```python
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
            assert False

@then(u'result should contain "./bin/find.py" file')
def step_impl(context):
        assert False
```


Run 'behave' and see it failing due to following error
```python
NameError: global name 'Findapp' is not defined
```

Now create bin/find.py file, make the first test pass

```python
#!/usr/bin/env python
import os
import sys
import re

class Findapp:
        def __init__(self, directory, pattern):
                self.directory = directory
                self.pattern = pattern
```


Run 'behave' command again and see the first test passing.

Accordingly you can develop your steps definition file and code. End of the goal is to make all tests pass.

Final snippet of "steps/findapp_steps.py" file
```python
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
```

**find** application "bin/find.py" file
```python
#!/usr/bin/env python
import os
import sys
import re

class Findapp:
	def __init__(self, directory, pattern):
		self.directory = directory
		self.pattern = pattern
	def find_impl(self):
		self.result = []
		expression = re.compile(self.pattern)
		for root, dirs, filename in os.walk(self.directory):
			for fname in filename:
				if expression.search(fname):
					filepath = os.path.join(root, fname)
					print filepath
					self.result.append(filepath)

if __name__ == '__main__':
	directory = sys.argv[1]
	pattern = sys.argv[3]
	j = Findapp(directory, pattern)
	j.find_impl()
```

Eventhough I've skipped many steps. Hope this information is sufficient to start with python BDD. 
