# DouyinLiveRecorder Skill

抖音直播流录制工具，基于 [DouyinLiveRecorder](https://github.com/leiweiba/DouyinLiveRecorder) v4.0.7。

## 功能

- 自动录制抖音直播流（视频+音频）
- 支持同时录制多个直播间
- 自动停止：直播结束或 22:00 自动停止

## 快速开始

### 1. 安装 Python 依赖

```bash
pip install -r requirements.txt
```

> 本 skill 的录制逻辑仅使用 Python 标准库，无需额外依赖。

### 2. 配置 Cookie

编辑 ```config/cookies.txt```，填入抖音登录 Cookie。

获取方式：浏览器登录抖音 → F12 → Network → 任意请求 → 复制 Cookie 头。

### 3. 配置直播间地址

编辑 ```config/URL_config.ini```，每行一个直播间 URL：

```
https://live.douyin.com/suoluosi1818
```

### 4. 开始录制

```bash
python scripts/record.py
```

或直接运行 ```DouyinLiveRecorder.exe```

## 目录结构

```
├── DouyinLiveRecorder.exe   # 录制工具主程序
├── _internal/               # 工具运行时依赖
├── ffmpeg/                  # 音视频处理工具
├── config/
│   ├── cookies.txt          # 抖音 Cookie（需配置）
│   └── URL_config.ini       # 直播间地址（需配置）
├── scripts/
│   └── record.py            # Python 录制脚本
├── SKILL.md                 # Skill 描述文件
└── requirements.txt
```

## 注意事项

- **Windows only**：DouyinLiveRecorder.exe 仅支持 Windows
- Cookie 过期后需重新获取
- 录制文件保存在 ```downloads/``` 目录
- 22:00 自动停止录制（可在 SKILL.md 中修改）
