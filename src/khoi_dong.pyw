# -*- coding: utf-8 -*-
"""SIÊU HỌC TIẾNG ANH – khởi động (biểu tượng Desktop / Start Menu trỏ vào file này).

Chỉ mở MỘT cửa sổ. Đã mở sẵn thì bấm lại chỉ đưa cửa sổ cũ lên. Cửa sổ dùng Microsoft Edge
ở chế độ ứng dụng (không thanh địa chỉ); không có Edge thì dùng trình duyệt mặc định.
Đóng cửa sổ là tắt phần mềm."""
import json
import os
import socket
import subprocess
import sys
import time
import traceback
import urllib.request
from pathlib import Path

GOC = Path(__file__).resolve().parent
sys.path.insert(0, str(GOC))
CONG_KHOA = 8830          # cổng "khóa" chống mở trùng


def _ghi_loi(s):
    try:
        import app
        d = app.DU_LIEU
    except Exception:
        d = GOC
    try:
        Path(d).mkdir(parents=True, exist_ok=True)
        with open(Path(d) / "nhat_ky_phan_mem.txt", "a", encoding="utf-8") as f:
            f.write(time.strftime("%d/%m/%Y %H:%M:%S ") + s + "\n")
    except Exception:
        pass


def tim_url_dang_chay():
    for cong in range(8831, 8852):
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{cong}/api/thong_tin", timeout=0.4) as r:
                if json.loads(r.read().decode("utf-8")).get("ung_dung") == "HOC_TIENG_ANH":
                    return f"http://127.0.0.1:{cong}/"
        except Exception:
            continue
    return None


def tim_edge():
    for p in (r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe",
              r"%ProgramFiles%\Microsoft\Edge\Application\msedge.exe",
              r"%LocalAppData%\Microsoft\Edge\Application\msedge.exe",
              r"%ProgramFiles%\Google\Chrome\Application\chrome.exe",
              r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"):
        q = os.path.expandvars(p)
        if os.path.exists(q):
            return q
    return None


def mo_cua_so(url):
    edge = tim_edge()
    if edge:
        import shutil
        ho_so = Path(os.environ.get("LOCALAPPDATA", str(GOC))) / "HOC_TIENG_ANH" / "cua_so"
        try:
            shutil.rmtree(ho_so, ignore_errors=True)
            ho_so.mkdir(parents=True, exist_ok=True)
        except Exception:
            pass
        subprocess.Popen([edge, f"--app={url}", "--window-size=1060,780", f"--user-data-dir={ho_so}",
                          "--new-window", "--no-first-run", "--no-default-browser-check",
                          "--disable-session-crashed-bubble", "--hide-crash-restore-bubble",
                          "--disable-features=Translate,InfiniteSessionRestore"])
    else:
        import webbrowser
        webbrowser.open(url)


def main():
    khoa = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        khoa.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
        khoa.bind(("127.0.0.1", CONG_KHOA))
        khoa.listen(1)
    except OSError:
        url = tim_url_dang_chay()
        if url:
            mo_cua_so(url)
        return

    import app
    try:
        sv, url = app.khoi_dong_may_chu()
    except BaseException:
        _ghi_loi("Khong mo duoc may chu:\n" + traceback.format_exc())
        raise
    mo_cua_so(url)

    bat_dau = time.time()
    while not app.TRANG["thoat"].is_set():
        time.sleep(2)
        song = app.TRANG["song"]
        if (song and time.time() - song > 25) or (not song and time.time() - bat_dau > 180):
            break
    try:
        sv.shutdown()
    except Exception:
        pass
    khoa.close()


if __name__ == "__main__":
    main()
