# example-etl

## 1. Overview

This is my first etl project!

## 2. Usage

### 2.1 init project

```bash
poetry install -v
```

### 2.2 usage

TODO

## 3. Develop

You may need to read the [develop document](./docs/development.md) to use SRC Layout in your IDE.


## 注意：使用poetry install -v 创建虚拟环境Python的版本不正确问题

1、检查环境中是否安装了其它版本的Python，如果有在环境变量的Path中将不需要的Python版本路径去掉；

2、检查pyproject.toml的Python版本设置是否正确；

3、检查poetry工具是否是在对应的Python版本中安装；

## poetry 使用命令

[Poetry的帮助使用指南文档](https://gitcode.com/GeekFong/how_to_use_poetry/blob/main/How_To_Use_Poetry/Poetry%E7%9A%84%E5%B8%AE%E5%8A%A9%E6%96%87%E6%A1%A3.md)

```
poetry   -V
Poetry (version 1.6.0)

poetry config --list --ansi #可以看出输出的文字是有颜色的
poetry config --list --no-ansi #可以看出输出的文字是有全是白色的

poetry init -n 初始化一个项目，如果不加-n就会询问你项目名和版本之类的

下面两个我基本是没有用到过
poetry install --no-plugins 通常在安装包的时候用，加快依赖安装速度
poetry install --no-cache 禁用缓存。相当于从源中重新安装

poetry -C的用法：设置输出目录
poetry init -C . #在当前目录建立

poetry -v 或 -vv 或 -vvv 用法：主要是输出的信息v越多，输出的调试信息越多，有点类似于logger等级
```

### 命令部分

```
可用命令:
  about              显示有关 Poetry 的信息。
  add                向 pyproject.toml 添加新的依赖项。
  build              默认情况下，构建一个包，作为 tarball 和 wheel。
  check              检查 pyproject.toml 文件的有效性。
  config             管理配置设置。
  export             将锁定文件导出到其他格式。
  help               显示命令的帮助信息。
  init               在当前目录中创建一个基本的 pyproject.toml 文件。
  install            安装项目的依赖项。
  list               列出命令。
  lock               锁定项目的依赖项。
  new                在 <path> 处创建一个新的 Python 项目。
  publish            将包发布到远程存储库。
  remove             从项目依赖项中删除包。
  run                在适当的环境中运行命令。
  search             在远程存储库上搜索包。
  shell              在虚拟环境中生成一个 shell。
  show               显示有关包的信息。
  update             根据 pyproject.toml 文件更新依赖项。
  version            显示项目的版本或根据提供的有效版本规则增加版本号。

cache
  cache clear        按名称清除 Poetry 缓存。
  cache list         列出 Poetry 的缓存。

debug
  debug info         显示调试信息。
  debug resolve      调试依赖关系解析。

env
  env info           显示有关当前环境的信息。
  env list           列出与当前项目关联的所有虚拟环境。
  env remove         删除与项目关联的虚拟环境。
  env use            激活或创建当前项目的新虚拟环境。

self
  self add           向 Poetry 运行时环境添加其他包。
  self install       安装此 Poetry 安装所需的已锁定包（包括附加组件）。
  self lock          锁定 Poetry 安装的系统要求。
  self remove        从 Poetry 运行时环境中删除其他包。
  self show          显示 Poetry 运行时环境中的包信息。
  self show plugins  显示当前安装的插件信息。
  self update        更新 Poetry 到最新版本。

source
  source add         为项目添加源配置。
  source remove      删除项目配置的源。
  source show        显示为项目配置的源信息。

```

### poetry config 管理配置设置,这个比较关键，下面会详细讲解

```
用-h查看其用法
poetry config -h

Description:
  Manages configuration settings.

Usage:
  config [options] [--] [<key> [<value>...]]

Arguments:
  key                        Setting key.
  value                      Setting value.

Options:
      --list                 List configuration settings.
      --unset                Unset configuration setting.
      --local                Set/Get from the project's local configuration.
  -h, --help                 Display help for the given command. When no command is given display help for the list command.
  -q, --quiet                Do not output any message.
  -V, --version              Display this application version.
      --ansi                 Force ANSI output.
      --no-ansi              Disable ANSI output.
  -n, --no-interaction       Do not ask any interactive question.
      --no-plugins           Disables plugins.
      --no-cache             Disables Poetry source caches.
  -C, --directory=DIRECTORY  The working directory for the Poetry command (defaults to the current working directory).
  -v|vv|vvv, --verbose       Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug.


poetry config --list  #查看当前配置

poetry config --list
cache-dir = "C:\\Users\\LisinPC\\AppData\\Local\\pypoetry\\Cache"
experimental.system-git-client = false
installer.max-workers = null
installer.modern-installation = true
installer.no-binary = null
installer.parallel = true
virtualenvs.create = true
virtualenvs.in-project = false
virtualenvs.options.always-copy = false
virtualenvs.options.no-pip = false
virtualenvs.options.no-setuptools = false
virtualenvs.options.system-site-packages = false
virtualenvs.path = "{cache-dir}\\virtualenvs"  # C:\Users\LisinPC\AppData\Local\pypoetry\Cache\virtualenvs
virtualenvs.prefer-active-python = false
virtualenvs.prompt = "{project_name}-py{python_version}"

cache-dir:缓存目录,用于存储项目依赖和虚拟环境等缓存信息。
experimental.system-git-client:是否使用系统自带的git客户端,false表示使用Poetry内置的git客户端。
installer.max-workers:安装依赖时的最大线程数,null表示使用默认线程数。
installer.modern-installation:是否使用Poetry的现代安装方案,true表示使用。
installer.no-binary:是否不使用预编译的二进制包,null表示不限制。
installer.parallel:是否并行安装依赖,true表示并行安装
virtualenvs.create:是否自动创建虚拟环境,true表示创建
virtualenvs.in-project:是否在项目内创建虚拟环境,true表示在项目中创建。
virtualenvs.options:虚拟环境创建时的选项配置，是否安装pip，是否安装setuptools，system-site-packages配置选项控制虚拟环境是否可以访问系统 site-packages 目录。默认情况下，此选项设置为 false，这意味着虚拟环境只能访问通过 Poetry 安装的包
virtualenvs.path:虚拟环境存放的路径
virtualenvs.prefer-active-python:是否优先使用系统激活的Python解释器
virtualenvs.prompt:虚拟环境的命令提示格式。

# 是这样使用的，比如设置虚拟环境在当前目录
poetry config virtualenvs.in-project true

```
