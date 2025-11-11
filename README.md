`git add <path_to_file>` </br>
`git commit -m '<your_msg>'`

`git branch <branch_name>` - create a new branch </br>
`git checkout -b <branch_name>` - create a new branch a switch to it


## Database
`alembic init migrations` - run once to init migration engine

`alembic revision --autogenerate -m "<your_migration_message>"` - create migration scenario
`alembic upgrade head` - run migrations scripts
