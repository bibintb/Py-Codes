# Data Preprocessing Stages 

Count NaN for entire dataframe

```
df.isnull().sum().sum()
```

Check values under column 

```
df['Column name'].isnull().values.any()
```

Count values under column

```
df['Column name'].isnull().sum()
```

Replace NaN values with zeros

```
df.fillna(0)
``` 

Check for NaN values in df

```
df.isnull().sum().sum()
```

Replace NaN values with zeros for a single column 

```
df['Column Name'] = df['Column Name'].fillna(0)
```

Replace NaN values with zeros for an entire Dataframe  
 
 ```
 df.fillna(0)
 ```
 
Remove Duplicates from Pandas DataFrame

```
df.drop_duplicates()
```  

Drop rows with all zeros in pandas data frame

```
df = df[(df.T != 0).any()]
```


