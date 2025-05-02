<div align="center">
    <picture>
      <source media="(prefers-color-scheme: light)" srcset="images/endtrace-light.svg">
      <source media="(prefers-color-scheme: dark)" srcset="images/endtrace-dark.svg">
      <img src="images/endtrace-light.svg" alt="endtrace" width="350" height="70" style="max-width: 100%;">
    </picture>
</div>

<p align="center">
    A command-line tool that locates Minecraft strongholds
</p>

<p align="center">
    <img src="https://img.shields.io/github/languages/top/justmaso/endtrace?color=%234E8386" alt="top language in the repository">
    <img src="https://img.shields.io/github/languages/code-size/justmaso/endtrace?color=%234E8386" alt="code size">
    <a href="https://github.com/justmaso/endtrace/blob/main/LICENSE"><img src="https://img.shields.io/github/license/justmaso/endtrace?color=%234E8386" alt="license"></a>
</p>

---

## About
A lightweight Python command-line tool that locates Minecraft strongholds using data from two Eye of Ender throws. Easily obtain stronghold coordinates and visualize the prediction if desired.


## Installation
Using [`pip`](https://pypi.org/project/pip/):
```
git clone https://github.com/justmaso/endtrace.git
cd endtrace
pip install -r requirements.txt
```

Using [`conda`](https://anaconda.org/anaconda/conda):
```
git clone https://github.com/justmaso/endtrace.git
cd endtrace
conda install --file requirements.txt
```


## Usage
### Command-Line Reference
```
usage: endtrace [-h] [-g] x1 z1 theta1 x2 z2 theta2

approximates the location of minecraft strongholds

positional arguments:
  x1           the x-coord of your first throw
  z1           the z-coord of your first throw
  theta1       the angle of your first throw (in degrees)
  x2           the x-coord of your second throw
  z2           the z-coord of your second throw
  theta2       the angle of your second throw (in degrees)

options:
  -h, --help   show this help message and exit
  -g, --graph  show a graph of the endtrace stronghold prediction
```

### Gathering Data from Eye of Ender Throws:
1. Open the debug screen by pressing <kbd>F3</kbd> on your keyboard
2. Throw an Eye of Ender
3. Center your crosshair over the thrown Eye of Ender
4. Gather the necessary data for the prediction to work (i.e., `x`, `z`, `theta`):

![debug screen](images/endtrace-throw-example.png)


## Example
Once you've collected throw data from distinct and sufficiently distant Eye of Ender throws, enter it into the command line as follows:

```
python endtrace.py 0.586 0.512 109.9 -350.193 0.226 115 --graph
predicted stronghold coords: (x=-1564.75, y=?, z=-566.13)
```

The above example produces the following visualization by using the `--graph` flag:

<p align="center">
    <img width="100%" src="images/endtrace-example.png">
</p>
