# Not your Type! Detecting Storage Collision Vulnerabilities in Ethereum Smart Contracts reproduction

## 复现指南 (Reproduction Guide)

本节记录了基于 Ubuntu 环境成功复现论文结果所需的详细步骤。

### 1. 环境搭建

**前置要求:**
- Python 3.10+ (建议使用虚拟环境)
- `jq` 和 `curl` (脚本依赖)
- `yices` SMT 求解器 (必须安装 2.6.2 版本以获取兼容的动态库)

**安装步骤:**

```bash
# 1. 克隆仓库
git clone https://github.com/glmgbj233/crush-reproduction.git
cd crush-reproduction

# 2. 创建并激活虚拟环境
python3 -m venv venv
source venv/bin/activate

# 3. 安装 Python 依赖
# 注意：我们指定了特定版本以确保兼容性
pip install . 
# 如果遇到 web3 方法报错 (如 is_connected vs isConnected)，
# 请应用本仓库提交历史中提供的补丁。

# 4. 安装 Yices SMT 求解器
# 安装 Python 绑定
pip install yices==1.1.3
# 安装系统库 (Yices 2.6.2)
# 下载 yices-2.6.2-x86_64-pc-linux-gnu-static-gmp.tar.gz
# 解压并运行 sudo ./install-yices

# 5. 安装 ethpwn
sudo pip install ethpwn
```

### 2. 配置说明

**Web3 兼容性:**
本复现解决了 `web3.py` v6+ 与项目使用的 snake_case 方法之间的兼容性问题。主要补丁包括：
- 将 `w3.isConnected()` 替换为 `w3.is_connected()` (或反之，取决于版本)
- 更新 `toChecksumAddress` 的用法。

### 3. 运行复现

执行以下命令对代理合约 `0x4DEcA...` 进行特定的漏洞分析：

```bash
# 运行完整分析流程
./crush.sh --proxy 0x4DEcA517D6817B6510798b7328F2314d3003AbAC --data ./data.example
```

### 4. 结果验证

分析结果将生成在 `data.example/` 目录下：
- **攻击报告**: `data.example/exploit/*.json` 包含生成的攻击载荷和验证日志。
- **类型分析**: `data.example/type/*.json` 显示推断出的每个合约的存储类型。
- **成功标志**: 在 exploit 日志中查找 `SENSITIVE TYPE_CONFUSION` 警告信息。

---
