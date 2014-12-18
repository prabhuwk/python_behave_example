Python BDD Example
=========

This is python behavior driven development example for **find** command.

find command is not fully featured. Purpose is to demonstrate BDD.

We are using python and behave to drive the BDD.
Assuming that python, behave, hamcrest are already installed.

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

4 directories, 5 files
```


Create a .feature file. I'm not going through details of .feature file.

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


Now modify your to fit your first step

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


run 'behave' and see it failing due to following error
NameError: global name 'Findapp' is not defined


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


run 'behave' command again and see the first test passing.

Accordingly you can develop your steps definition file and code. End of the goal is to make all tests pass.

final snippet of "steps/findapp_steps.py" file
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


'behave' command output snippet
``` cucumber
Feature: Implementing unix find command # features/findapp.feature:1

Scenario Outline: unix find command               # features/findapp.feature:2
Given name of "." and ".*.py"                   # steps/findapp_steps.py:7 0.000s
When I execute definition                       # steps/findapp_steps.py:13 0.001s
Then result should contain "./bin/find.py" file # steps/findapp_steps.py:17 0.000s

Scenario Outline: unix find command                  # features/findapp.feature:2
Given name of "/etc" and ".*.bash"                 # steps/findapp_steps.py:7 0.000s
When I execute definition                          # steps/findapp_steps.py:13 0.039s
Then result should contain "/etc/bash.bashrc" file # steps/findapp_steps.py:17 0.000s

1 feature passed, 0 failed, 0 skipped
2 scenarios passed, 0 failed, 0 skipped
6 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.041s
```

Eventhough I've skipped many steps. Hope this information is sufficient to start with python BDD. 

