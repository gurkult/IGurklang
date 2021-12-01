# IGurklang
Jupyter kernel for gurklang

# Setup
clone the repo and navigate to it
```
$ pip install  git+https://github.com/gurkult/py-gurklang.git@lakmatiol/packaging
$ pip install .
```
then, to start, run
```
$ python -m igurklang.kernel
```
this will output
```
...
To connect another client to this kernel, use:
    --existing kernel-number.json
```
then use `ipython console --existing kernel-number.json`