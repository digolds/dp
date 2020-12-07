# An easy-to-use data manipulation framework for data analysts

dp(data pipeline) is mainly focus on handling automation of a data analyst's daily routines, such as merging thousand of cvs files into single xlsx file in just  several minutes, ploting diagrams when new data is arrived. As a data analyst, you can use dp to build your data pipeline, which will bring your data, and turn that into insightful reports automatically.

More features will add to dp, I'm happy to know what real problems you(as a data analyst) are struggling for and what ablities you are expecting to extend, so that you can process data in an easy way!

In order to use dp, firstly, you should install it by `pip install digolds-dp`, after installed, type the following command to check the version:

```bash
dp --version
```

The outut is shown below:

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