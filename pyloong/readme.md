<!-- markdownlint-disable MD040 -->

# pyloong 说明

## 网址

```

https://pyloong.github.io/pythonic-project-guidelines/
```

# cookiecutter 项目创建

```
https://github.com/pyloong/cookiecutter-pythonic-project
```

## 安装

```
# 安装或升级 cookiecutter
pip install -U cookiecutter

# 使用 cookiecutter 加载项目模板，生成项目
# 回车运行的时候，需要根据提示交互选择启用的功能。
# 如果使用默认配置，则一路回车就可以。
cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
```

## 创建项目

```
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
project_name [My Project]:
project_slug [my_project]:
project_description [My Awesome Project!]:
author_name [Author]:
author_email [author@example.com]:
version [0.1.0]:
Select python_version:
1 - 3.10
2 - 3.11
Choose from 1, 2 [1]:
use_src_layout [y]:
use_poetry [y]:
use_docker [n]:
Select ci_tools:
1 - none
2 - Gitlab
3 - Github
Choose from 1, 2, 3 [1]:
init_skeleton [n]:
```
