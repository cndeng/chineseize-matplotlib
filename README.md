
# chineseize-matplotlib
自动设置 matplotlib 中文字体

## 利用方法

```python
import matplotlib.pyplot as plt
import chineseize_matplotlib

plt.plot([1, 2, 3, 4])
plt.xlabel('简单图表')
plt.show()
```


## 安装
```sh
# pipenv
pipenv install chineseize-matplotlib

# pip
pip install chineseize-matplotlib
```

##使用字体

使用IPA字体的IPAex黑体(Ver.003.01)。

利用进程[ipa字体授权v 1.0] (https://github.com/cndeng/chineseize-matplotlib/blob/master/chineseize_matplotlib/fonts/ipa_font_license_agreement_v1.0.txt)请同意。