import pandas 

row_oriented_data = [
    [1, 2, 3],
    [4, 5, 6],
    [6, 1, 4]
]


row_oriented_dict_data = [
    {"c1": 1, "c2": 2, "c3": 4},
    {"c1": 6, "c2": 3, "c3": 7},
    {"c1": 7, "c2": 3, "c3": 4}
]

column_oriented_data = {
    "c1": [1, 2, 3],
    "c2": [2, 4, 7],
    "c3": [4, 2, 1]
}

# data frame from row_oriented_data
df1 = pandas.DataFrame(row_oriented_data)
print(df1)

# extract a column
col_series = df1[0]
print(col_series)

# extract a row
row_series = df1.loc[1]
print(row_series)

# grab an element
element = df1.loc[0, 2]
print(element)


# data fram from row_oriented_dict_data
df2 = pandas.DataFrame(row_oriented_dict_data)
print(df2)

# extract a column
col_series = df2["c2"]
print(col_series)

# extract a row
row_series = df2.loc[2]
print(row_series)

# grab an element
element = df2.loc[2, "c3"]
print(element)

# grab a column with loc (or a range of rows or columns)
col_series = df2.loc[:, "c3"]
print(col_series)