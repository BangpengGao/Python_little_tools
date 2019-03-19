# -*- coding: utf-8 -*-
# @Author: Phill
# @Date:   2019-03-18 17:27:18
# @Last Modified by:   Phill
# @Last Modified time: 2019-03-18 17:29:48

import importlib
aa = importlib.import_module("fileRW")
print(aa.dictToList({1:1,2:2}))
