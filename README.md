# Douyin Live Recorder

抖音直播流录制工具。使用 [DouyinLiveRecorder](https://github.com/leiweiba/DouyinLiveRecorder) 直接录制直播流，支持多平台和循环值守。

## 快速开始

### 1. 配置直播间地址

编辑 `config/URL_config.ini`，添加直播间地址：

```ini
https://live.douyin.com/直播间ID
```

### 2. 配置 Cookie（必需）

编辑 `config/cookies.txt`，填入抖音 Cookie：

1. 浏览器打开抖音并登录
2. 按 F12 打开开发者工具
3. 切换到 Network 标签
4. 刷新页面，找到任意请求
5. 复制 Request Headers 中的 Cookie 值

### 3. 运行录制

```powershell
cd DouyinLiveRecorder_v4.0.7
python run_recorder_single.exe
```

## 输出位置

录制的视频文件保存在 `Downloads/` 目录，格式为 `.ts` 或 `.flv`。

## 提取音频

```powershell
ffmpeg -i "视频文件.ts" -vn -acodec libmp3lame -ab 128k "输出.mp3"
```

## 支持平台

抖音、快手、B站等 40+ 平台。

## 注意事项

- 需要有效的抖音 Cookie，否则无法获取直播流
- 直播间必须正在直播才能录制