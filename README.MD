# An easy-to-use data manipulation framework for data analysts

## Quick guide

dp(data pipeline) is mainly focus on handling automation of a data analyst's daily routines, such as merging thousand of cvs files into single xlsx file in just  several minutes, ploting diagrams when new data is arrived. As a data analyst, you can use dp to build your data pipeline, which will bring your data, and turn that into insightful reports automatically.

More features will add to dp, I'm happy to know what real problems you(as a data analyst) are struggling for and what ablities you are expecting to extend, so that you can process data in an easy way!

In order to use dp, firstly, you should install it by `pip install digolds-dp`, after installed, type the following command to check the version:

```bash
dp --version
```

The output is shown below:

```bash
dp(data pipeline) 0.0.2
```

dp is designed with the following principles in mind:

```bash
dp <operation> <sub-command> <options>
```

For example, you can merge a large number of csv files into single xlsx file by the following command:

```bash
dp merge multi-csv2xlsx --src-path D:\tests --xlsx-file D:\final.xlsx --sheet-name daily
```

The operation types are shown below:

1. `merge`, you should use it for merging data
2. `draw`, you should use it for plotting diagrams

You can also enter the following command to learn more from some articles:

```bash
dp --help
```

## Unit Test

* Run all unit tests by typing the following command in Terminal.

```bash
python -m unittest discover -v -s tests
```

* Run specific test by typing the following command in Terminal.

```bash
python -m unittest -v <module-name>

For example
python3 -m unittest -v tests/test_common.py
```

## Delpoy locally

Visit [here](https://packaging.python.org/tutorials/packaging-projects/) to learn how to package a lib step by step.

* Run the following command to build .whl file:

```bash
python3 -m build
```

* Run the following command to uninstall the previous version

```bash
pip3 uninstall digolds-dp
```

* Run the following command to install new version

```bash
pip3 install dist/digolds_dp-0.0.2-py3-none-any.whl
```