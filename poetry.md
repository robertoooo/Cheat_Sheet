Set this setting if you want to create a venv inside your working directory:
```sh
poetry config virtualenvs.in-project true
```

Update and install from the toml file
```sh
poetry update
poetry install
```

Open a shell or enter an already opened shell
```sh
poetry shell
source $(poetry env info --path)/bin/activate
```

List or delete poetry env
```sh
poetry env list
poetry env remove <name-of-env>
```
