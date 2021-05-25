# DataITO

![Python Logo](https://www.python.org/static/community_logos/python-logo.png "Sample inline image")

<center><img src="https://camo.githubusercontent.com/8ea5ab2f59ce09a175cb2fd87d0a75b86bde024cbb8b96a596f9d698a89dea15/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f707972696768742d4d49542d677265656e"><img src="https://camo.githubusercontent.com/036c3fa7badfd718f1d5f594921b9eeb0f3122a0529d3f4113aeb584cae74f1b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d646174612d626c7565"></center>

## 安装(install)

- 安装开发版（Install development version）

```python
py -m pip install --index-url https://test.pypi.org/simple/ --no-deps dataito
```

- 安装版（ Install stable version ）

```python
pip install dataito		# 暂未发布（Not released yet）
```



## cn

Python数据输入(Input)、转换(transform)、输出(output)，一行代码读取/转换多种格式的数据文件

- 目前支持的读取格式

  - txt
  - xlsx
  - csv
  - json（仅支持结构化数据）

- 目前支持的转换格式

  - dataframe (pandas)
  - array (numpy)
  - list

- 目前支持的保存格式

  - xlsx（目前仅支持保存为xlsx，在考虑是否要增加自定义格式保存功能）

- example

  ```python
  import dataito
  
  filepath = r'data/data.xlsx'				#读取支持格式的数据文件
  data = dataito.read(filepath)				#调用函数读取(读取其他支持的格式也是这个函数)
  data= dataito.transform(data,'dataframe')	#数据格式转换为想要的格式（转换为其他支持的格式也是这个）
  save(data,r'D:\data')	#保存在data文件夹（默认文件名为data）
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
    save(data,r'D:\data')	#Save in the data folder (the default file name is data). If the path is not written, the file is saved in the root directory
  ```
  
  

  

