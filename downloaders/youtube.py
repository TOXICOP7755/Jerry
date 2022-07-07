from os import path

from yt_dlp import YoutubeDL

from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio/best",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)
    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f" ❌𝚅𝙸𝙳𝙴𝙾𝚂 𝙻𝙾𝙽𝙶𝙴𝚁 𝚃𝙷𝙰𝙽 {DURATION_LIMIT} 𝙼𝙸𝙽𝚄𝚃𝙴(𝚂) 𝙰𝚁𝙴𝙽'𝚃 𝙰𝙻𝙻𝙾𝚆𝙴𝙳, 𝚃𝙷𝙴 𝙿𝚁𝙾𝚅𝙸𝙳𝙴𝙳 𝚅𝙸𝙳𝙴𝙾 𝙸𝚂 {duration} 𝙼𝙸𝙽𝚄𝚃𝙴(𝚂) ",
        )
    try:
        ydl.download([url])
    except:
        raise DurationLimitError(
            f" ❌𝚅𝙸𝙳𝙴𝙾𝚂 𝙻𝙾𝙽𝙶𝙴𝚁 𝚃𝙷𝙰𝙽 {DURATION_LIMIT} 𝙼𝙸𝙽𝚄𝚃𝙴(𝚂) 𝙰𝚁𝙴𝙽'𝚃 𝙰𝙻𝙻𝙾𝚆𝙴𝙳, 𝚃𝙷𝙴 𝙿𝚁𝙾𝚅𝙸𝙳𝙴𝙳 𝚅𝙸𝙳𝙴𝙾 𝙸𝚂 {duration} 𝙼𝙸𝙽𝚄𝚃𝙴(𝚂) ",
   )
    return path.join("downloads", f"{info['id']}.{info['ext']}")
