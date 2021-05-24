# DataITO

![copyright: MIT (shields.io)](https://img.shields.io/badge/copyright-MIT-green)![python: data (shields.io)](https://img.shields.io/badge/python-data-blue)

## cn

Python数据输入(Input)、转换(transform)、输出(output)，一行代码读取/转换多种格式的数据文件



- 目前支持的读取格式

  - txt
  - xlsx
  - csv

- 目前支持的转换格式

  - dataframe

  

- example

  ```python
  import dataito
  
  filepath = r'data/data.xlsx'				#读取支持格式的数据文件
  data = dataito.read(filepath)				#调用函数读取(读取其他支持的格式也是这个函数)
  data= dataito.transform(data,'dataframe')	#数据格式转换为想要的格式（转换为其他支持的格式也是这个）
  ```

  



## en

Python data input (i), transform (t), output (o), a line of code to read / convert a variety of formats of data files

- Currently supported read formats

  - txt
  - xlsx
  - csv

- Currently supported conversion formats

  - dataframe

  

- example

  ```python
  import dataito
  
  filepath = r'data/data.xlsx'				#Read data files in supported formats
  data = dataito.read(filepath)				#Call the function to read (read other supported formats as well as this function)
  data= dataito.transform(data,'dataframe')	#Convert the data format to the desired format (and other supported formats)
  ```

  