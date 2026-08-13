# C语言课程GNU GCC环境配置

本教程帮助学生在Windows 10/11、macOS和Linux上配置真正的GNU GCC，并在VS Code中完成C程序的编辑、编译和运行。三类平台都可以编译标准C程序；仓库的完整自动校验仍以Windows MinGW-w64和GitHub Actions为准。

## 通用准备

1. 安装[Visual Studio Code](https://code.visualstudio.com/)。
2. 在扩展市场安装Microsoft发布的`C/C++`扩展。
3. 新建`hello.c`：

```c
#include <stdio.h>

int main()
{
    printf("Hello World\n");

    return 0;
}
```

安装编译器后，应同时检查命令位置、版本和目标平台，不要只观察命令是否存在。

## Windows 10/11

### 1. 下载并核对MinGW-w64

从[SourceForge官方目录](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/8.1.0/threads-posix/seh/x86_64-8.1.0-release-posix-seh-rt_v6-rev0.7z)下载：

```text
x86_64-8.1.0-release-posix-seh-rt_v6-rev0.7z
```

该课程基线压缩包的SHA-256为：

```text
853970527B5DE4A55EC8CA4D3FD732C00AE1C69974CC930C82604396D43E79F8
```

在下载目录打开PowerShell并核对：

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath ".\x86_64-8.1.0-release-posix-seh-rt_v6-rev0.7z"
```

输出必须与上述值完全一致。

### 2. 解压并配置Path

将压缩包解压到固定且不含中文、空格或特殊字符的目录，例如：

```text
C:\mingw64
```

确认`C:\mingw64\bin\gcc.exe`存在，再把以下目录加入用户或系统环境变量`Path`：

```text
C:\mingw64\bin
```

关闭并重新打开PowerShell和VS Code，然后验证：

```powershell
Get-Command gcc
gcc --version
gcc -dumpmachine
```

`gcc -dumpmachine`的结果应包含：

```text
x86_64-w64-mingw32
```

### 3. 编译和运行

```powershell
gcc hello.c -o hello.exe
.\hello.exe
```

### 4. VS Code编译器路径

在命令面板中选择`C/C++: Edit Configurations (UI)`，将`Compiler path`设置为：

```text
C:\mingw64\bin\gcc.exe
```

## macOS：Homebrew GNU GCC

本节使用Homebrew提供的GNU Compiler Collection预编译包。课程环境只接受GNU GCC的身份检查结果。

### 1. 安装Homebrew

从[Homebrew安装文档](https://docs.brew.sh/Installation)进入官方`.pkg`安装器。默认前缀通常为：

- Apple Silicon：`/opt/homebrew`
- Intel：`/usr/local`

按照安装器最后显示的命令，把`brew shellenv`加入`~/.zprofile`，然后重新打开终端。若安装器不能使用预编译包并要求额外开发环境，请停止该路线并使用教师提供的已配置课程环境。

### 2. 安装GNU GCC

[Homebrew GCC公式](https://formulae.brew.sh/formula/gcc)提供GNU Compiler Collection：

```bash
brew install gcc
```

Homebrew安装的命令通常带主版本后缀，例如`gcc-16`。建立仅对当前用户生效的稳定`gcc`入口：

```bash
GCC_MAJOR="$(brew list --versions gcc | awk '{split($2, v, "."); print v[1]}')"
mkdir -p "$HOME/.local/bin"
ln -sf "$(brew --prefix)/bin/gcc-$GCC_MAJOR" "$HOME/.local/bin/gcc"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.zprofile"
source "$HOME/.zprofile"
```

### 3. 验证GNU GCC身份

```bash
command -v gcc
gcc --version
gcc -dumpmachine
```

验收结果：

- `command -v gcc`指向`$HOME/.local/bin/gcc`；
- 版本信息明确标识GNU GCC；
- `gcc -dumpmachine`显示当前macOS目标平台。

### 4. 编译和运行

```bash
gcc hello.c -o hello
./hello
```

### 5. VS Code编译器路径

先取得实际版本化编译器路径：

```bash
readlink "$HOME/.local/bin/gcc"
```

把该命令输出填入VS Code的`Compiler path`，例如Apple Silicon环境中的`/opt/homebrew/bin/gcc-16`，或Intel环境中的`/usr/local/bin/gcc-16`。版本号以本机实际输出为准。

## Linux

### Debian或Ubuntu

```bash
sudo apt update
sudo apt install build-essential gdb
```

### Fedora系列

```bash
sudo dnf install gcc gdb
```

### 验证、编译和运行

```bash
command -v gcc
gcc --version
gcc -dumpmachine
gcc hello.c -o hello
./hello
```

VS Code的`Compiler path`通常设置为：

```text
/usr/bin/gcc
```

具体界面可参考[VS Code C/C++ IntelliSense配置文档](https://code.visualstudio.com/docs/cpp/configure-intellisense)。

## 常见问题

### 找不到gcc命令

- 关闭并重新打开终端和VS Code，使新的`Path`生效。
- Windows使用`Get-Command gcc`，macOS和Linux使用`command -v gcc`检查实际命令来源。
- 检查配置的目录中是否存在真实的GCC可执行文件。

### 终端能够编译，VS Code仍显示红色波浪线

- 在`C/C++: Edit Configurations (UI)`中重新选择实际GCC路径。
- 重新加载VS Code窗口。
- 确认当前工作区没有遗留的错误`compilerPath`覆盖全局设置。

### 编译成功但运行命令失败

- Windows运行当前目录程序时使用`.\hello.exe`。
- macOS和Linux运行当前目录程序时使用`./hello`。
- 先观察编译命令是否已经生成对应文件。

## 课程环境与仓库校验边界

- Windows、macOS和Linux均使用GNU GCC完成标准C课程程序的编写与运行。
- Windows使用MinGW-w64目标；macOS和Linux使用各自的原生GNU GCC目标。
- `conio.h`、`getch()`等接口属于Windows/MinGW课程识别边界，在macOS和Linux上不作为可移植程序接口。
- 本仓库的全量例程、题库和上机任务单校验仍以Windows MinGW-w64目标为正式基线，并由Windows GitHub Actions进行向前兼容复验。
- macOS和Linux命令来自上述官方安装与配置资料；本仓库不声称已在当前Windows维护机上执行这些平台命令。
