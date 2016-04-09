# easypub
easyquant/easyhistory/easytrader/easyquant的公用模块

包含的package:

    stockcodes: 处理与股票代码表相关的功能

    (目前仅此一个)


### 引入

```python
import stockcodes
```
### 用法


### 更新代码表及各个分类代码表

```python
stockcodes.update_stock_codes()
```
更新后缺省代码表重置为全部代码表，如果希望缺省代码表为某个分类代码表， 需调用set_default_scope设置缺省代码表

### 获取代码表

```python
stockcodes.get_stock_codes(scope=['default'])
```
可以使用列表同时获取多个分类, scope=['all'] 可以获取全部代码表

scope=['default'] 获取当前缺省代码表

scope=['index','fund'] 获取指数及基金代码表

### 设置缺省代码表

```python
stockcodes.set_default_scope(scope=['all'])
```

### 查询代码对应的品种类型
```python
stock_type = stockcodes.code_type(stock_code)
```
返回值：

index, fund, bond, cb(可转债), eb(可交换债), repo(逆回购), fundnav(基金净值),bstock, astock, other

注：

目前使用的分类及对应的代码表文件有：

scopeandfile = {'all': 'stock_codes_all.conf',

              'index': 'stock_codes_idx.conf',

              'fund': 'stock_codes_fund.conf',

              'astock': 'stock_codes_astock.conf',

              'bstock': 'stock_codes_bstock.conf',

              'defulat': 'stock_codes.conf',

              'self': 'stock_codes_self.conf'

              }

其中self为自选代码表，自行编辑，update_stock_codes时不做更新，但可以读取。

