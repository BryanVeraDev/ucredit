@echo off

rem Define the commands for each action
set COMMAND_RUN=python manage.py runserver
set COMMAND_TEST=python manage.py test
set COMMAND_LINT=ruff check
set COMMAND_COVERAGE=coverage run --source='.\' manage.py test ^&^& coverage report
rem Check the first argument (the action to perform)
if "%1" == "run" (
    %COMMAND_RUN%
) else if "%1" == "test" (
    %COMMAND_TEST%
) else if "%1" == "lint" (
    %COMMAND_LINT%
) else if "%1" == "coverage" (
    %COMMAND_COVERAGE%
) else (
    echo Invalid command. Use 'run', 'test', 'lint', or 'coverage'.
)