Feature: Implementing unix find command
	Scenario Outline: unix find command
		Given name of "<directory>" and "<pattern>"
		When I execute definition
		Then result should contain "<expected_file>" file

		Examples: 
			| directory | pattern | expected_file |
			| .	    | .*.py   | ./bin/find.py |
			| /etc	    | .*.bash | /etc/bash.bashrc |
