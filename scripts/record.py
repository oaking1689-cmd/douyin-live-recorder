"""
抖音直播流录制脚本
使用 DouyinLiveRecorder 录制直播流
"""
import subprocess
import os
import sys

RECORDER_PATH = r"C:\Users\happy\.qclaw\tools\douyin-recorder\DouyinLiveRecorder_v4.0.7"
FFMPEG_PATH = os.path.join(RECORDER_PATH, "ffmpeg", "ffmpeg.exe")

def extract_audio(video_file: str, output_mp3: str = None) -> str:
    """从视频文件提取音频"""
    if output_mp3 is None:
        output_mp3 = video_file.rsplit('.', 1)[0] + '.mp3'
    
    cmd = [
        FFMPEG_PATH,
        '-i', video_file,
        '-vn',
        '-acodec', 'libmp3lame',
        '-ab', '128k',
        output_mp3,
        '-y'
    ]
    
    print(f"提取音频: {video_file} -> {output_mp3}")
    subprocess.run(cmd, check=True)
    return output_mp3

def check_audio_level(audio_file: str) -> dict:
    """检查音频电平"""
    cmd = [
        FFMPEG_PATH,
        '-i', audio_file,
        '-af', 'volumedetect',
        '-f', 'null', '-'
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
    output = result.stderr
    
    mean_vol = None
    max_vol = None
    
    for line in output.split('\n'):
        if 'mean_volume' in line:
            mean_vol = float(line.split(':')[1].strip().split()[0])
        if 'max_volume' in line:
            max_vol = float(line.split(':')[1].strip().split()[0])
    
    return {'mean_volume': mean_vol, 'max_volume': max_vol}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python record.py <视频文件> [输出mp3]")
        sys.exit(1)
    
    video_file = sys.argv[1]
    output_mp3 = sys.argv[2] if len(sys.argv) > 2 else None
    
    mp3_file = extract_audio(video_file, output_mp3)
    
    levels = check_audio_level(mp3_file)
    print(f"音频电平: mean={levels['mean_volume']}dB, max={levels['max_volume']}dB")
