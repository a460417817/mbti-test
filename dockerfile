# 使用官方Python镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录内容到工作目录
COPY . .

# 安装Python虚拟环境所需的包
RUN apt-get update && apt-get install -y python3-venv

# 创建虚拟环境
RUN python3 -m venv /app/venv

# 激活虚拟环境并安装依赖
RUN /app/venv/bin/pip install -r requirements.txt
RUN /app/venv/bin/pip install gunicorn

# 确保所有命令在虚拟环境中运行
ENV PATH="/app/venv/bin:$PATH"

# 暴露应用端口
EXPOSE 8000

# 启动应用
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "server:app"]

