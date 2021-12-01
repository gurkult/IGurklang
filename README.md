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
this will output something along the lines of
```
...
To connect another client to this kernel, use:
    --existing kernel-number.json
```
you can also install the kernel using
```
$ jupyter kernelspec install gurklang_kernel
```
then use `jupyter console --existing kernel-number.json`