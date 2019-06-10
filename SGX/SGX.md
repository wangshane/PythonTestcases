# SGX side channel文献综述

## 1. Intel SGX基础概念

       英特尔软件保护扩展（SGX）是一组安全相关的指令代码，内置于一些现代英特尔中央处理器（CPU）中。它们允许用户级和操作系统代码定义内存的私有区域，称为enclaves，其内容受到保护，无法被enclaves外的任何进程读取或保存，包括以更高权限级别运行的进程。默认情况下，SGX处于禁用状态，用户必须通过支持的系统上的BIOS设置选择使用SGX。SGX旨在实现安全的远程计算，安全的Web浏览和数字版权管理（DRM）。其他应用包括隐藏专有算法和加密密钥。

       SGX涉及CPU对一部分内存进行加密。enclave仅在CPU本身内即时解密，即使这样，也仅限于enclave内部运行的代码和数据。因此，处理器保护代码不被“窥探”或被其他代码检查。enclave中的代码和数据利用威胁模型，其中enclave受到信任，但不能信任其外的进程（包括操作系统本身和任何管理程序），因此所有这些都被视为潜在的威胁。enclave内的任何代码都无法读取除了加密形式外的enclave内容（如下图所示）。

![SGX isolation](SGX isolation.png)



## 2. SGX侧信道攻击

### 2.1

## 3. 攻击后果

## 4. 检测方法

## 5. 防御方法

## 6.

## 参考文献