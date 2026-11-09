# -*- coding: utf-8 -*-
"""SIÊU HỌC TIẾNG ANH – máy chủ giao diện (chạy tại máy, mở bằng cửa sổ như phần mềm Windows).

Toàn bộ bài học nằm trong giao diện (ui/index.html). Máy chủ chỉ phục vụ trang và LƯU TIẾN ĐỘ
vào thư mục người dùng (gỡ phần mềm không mất). Phát âm dùng giọng đọc sẵn của Windows (offline)."""
import json
import os
import sys
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

GOC = Path(__file__).resolve().parent
PHIEN_BAN = "1.0 (07/11/2026)"
DU_LIEU = Path.home() / "HOC_TIENG_ANH"
TEP_TIEN_DO = DU_LIEU / "tien_do.json"
TRANG = {"song": 0, "thoat": threading.Event()}


def _doc_tien_do():
    try:
        return json.loads(TEP_TIEN_DO.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _luu_tien_do(d):
    try:
        DU_LIEU.mkdir(parents=True, exist_ok=True)
        TEP_TIEN_DO.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
        return True
    except Exception:
        return False


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _tra(self, obj, ma=200, loai="application/json; charset=utf-8"):
        body = obj if isinstance(obj, bytes) else json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(ma)
        self.send_header("Content-Type", loai)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        try:
            if self.path in ("/", "/index.html"):
                return self._tra((GOC / "ui" / "index.html").read_bytes(), loai="text/html; charset=utf-8")
            if self.path == "/api/song":
                TRANG["song"] = time.time()
                return self._tra({"ok": True})
            if self.path == "/api/thong_tin":
                return self._tra({"ung_dung": "HOC_TIENG_ANH", "phien_ban": PHIEN_BAN})
            if self.path == "/api/tien_do":
                return self._tra({"tien_do": _doc_tien_do()})
            self._tra({"loi": "khong co"}, 404)
        except Exception as e:
            self._tra({"loi": str(e)}, 500)

    def do_POST(self):
        try:
            n = int(self.headers.get("Content-Length") or 0)
            d = json.loads(self.rfile.read(n).decode("utf-8") or "{}")
            if self.path == "/api/tien_do":
                return self._tra({"ok": _luu_tien_do(d.get("tien_do", {}))})
            if self.path == "/api/thoat":
                TRANG["thoat"].set()
                return self._tra({"ok": True})
            self._tra({"loi": "khong co"}, 404)
        except Exception as e:
            self._tra({"loi": str(e)}, 500)


def khoi_dong_may_chu():
    cong = int(os.environ.get("HTA_PORT", "8831"))
    for thu in range(20):
        try:
            sv = ThreadingHTTPServer(("127.0.0.1", cong + thu), H)
            break
        except OSError:
            continue
    else:
        raise SystemExit("Khong mo duoc cong.")
    threading.Thread(target=sv.serve_forever, daemon=True).start()
    return sv, f"http://127.0.0.1:{sv.server_port}/"


def main():
    sv, url = khoi_dong_may_chu()
    if "--khong-mo" not in sys.argv:
        webbrowser.open(url)
    print("SIEU HOC TIENG ANH dang chay:", url)
    bat_dau = time.time()
    while not TRANG["thoat"].is_set():
        time.sleep(2)
        song = TRANG["song"]
        if "--khong-mo" not in sys.argv and ((song and time.time() - song > 25) or (not song and time.time() - bat_dau > 180)):
            break
    sv.shutdown()


if __name__ == "__main__":
    main()
