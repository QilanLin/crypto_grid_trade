# 加密货币价格预警系统

这是一个基于 Python 的价格预警系统，能够监控 Binance 平台上的 MELANIA/USDT 交易对价格。当价格进入设定的区间时，系统会通过邮件方式发送通知。

---

## 功能介绍

- 获取 Binance 交易所中 MELANIA/USDT 交易对的最新价格
- 设定多个价格区间，当价格进入任意区间时触发预警
- 支持邮件通知，便于用户及时了解价格变化

---

## 使用方法

1. 克隆代码仓库并进入项目目录：
    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. 安装所需的 Python 依赖：
    ```bash
    pip install -r requirements.txt
    ```

3. 编辑配置文件 `config.py`，填入您的邮件账户、SMTP 设置及预警价格区间。

4. 启动程序：
    ```bash
    python main.py
    ```

