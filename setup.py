# -*- coding: utf-8 -*-
# Author: XuMing <xuming624@qq.com>
# Brief: 
from __future__ import print_function
from setuptools import setup, find_packages

long_description = '''
## Usage

### install
* pip install pycorrector / pip3 install pycorrector 
* Or download https://github.com/shibing624/corrector Unzip and run python setup.py install

### correct 
input:
```
import pycorrector

corrected_sent, detail = pycorrector.correct('少先队员因该为老人让坐')
print(corrected_sent, detail)

```

output:
```
少先队员应该为老人让座 [[('因该', '应该', 4, 6)], [('坐', '座', 10, 11)]]
```

----


# corrector
中文错别字纠正工具。音似、形似错字（或变体字）纠正，可用于中文拼音、笔画输入法的错误纠正。python开发。

**corrector**依据语言模型检测错别字位置，通过拼音音似特征、笔画五笔编辑距离特征及语言模型困惑度特征纠正错别字。

## 特征
### 语言模型
* Kenlm（统计语言模型工具）
* RNNLM（TensorFlow、PaddlePaddle均有实现栈式双向LSTM的语言模型）

## 使用说明

### 安装
* 全自动安装：pip install pycorrector 或者 pip3 install pycorrector 
* 半自动安装：下载 https://github.com/shibing624/corrector 解压缩并运行 python setup.py install

### 纠错 
使用示例:
```
import pycorrector

corrected_sent, detail = pycorrector.correct('少先队员因该为老人让坐')
print(corrected_sent, detail)

```

输出:
```
少先队员应该为老人让座 [[('因该', '应该', 4, 6)], [('坐', '座', 10, 11)]]
```  
    
'''

setup(
    name='pycorrector',
    version='0.1.2',
    description='Chinese Text Error corrector',
    long_description=long_description,
    author='XuMing',
    author_email='xuming624@qq.com',
    url='https://github.com/shibing624/corrector',
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='NLP,correction,Chinese error corrector,corrector',
    install_requires=[
        'kenlm==0.0.0',
        'numpy',
        'pypinyin',
        'jieba'
    ],
    packages=['pycorrector'],
    package_dir={'pycorrector': 'pycorrector'},
    package_data={
        'pycorrector': ['*.py', 'zhtools/*', 'LICENSE', 'README.*', 'data/*', 'data/kenlm/people_chars_lm.klm'],
    }
)
