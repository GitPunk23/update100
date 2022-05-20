#!/bin/bash

# - - - - - ENTER FILEPATH TO LOG FILE - - - - -
logFilePath=

# - - - - - ENTER FILEPATH TO UPDATE100.PY - - - - -
update100Path=

git add logFilePath 
git commit -m 'DOCS: Add New Day'
git push 
echo 'Update has been committed and pushed successfully!' 
python3 update100Path