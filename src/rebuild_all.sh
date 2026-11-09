#!/bin/bash
# Ráp nội dung -> HTML -> bộ cài .exe (NSIS) + .msi (wixl)
set -e
V=${1:-3.0.0}
cd /home/user/TOEIC_APP && python3 build.py | grep school
ST=/tmp/claude-0/stage_hta
cp SieuHocTOEIC.html $ST/HOC_TIENG_ANH/ui/index.html
cp SieuHocTOEIC.html /home/user/HOC_TIENG_ANH/ui/index.html
cd $ST && sed -i "s/^!define PHIEN_BAN .*/!define PHIEN_BAN \"$V\"/" cai_dat.nsi
LANG=C.UTF-8 makensis cai_dat.nsi >/dev/null 2>&1
M=/tmp/claude-0/msi; rm -rf $M/SieuHoc; cp -r $ST/HOC_TIENG_ANH $M/SieuHoc; cd $M
sed -i "s/Version=\"[0-9.]*\" Manufacturer/Version=\"$V\" Manufacturer/" main.wxs
find SieuHoc -type f | wixl-heat --prefix SieuHoc/ --component-group AppFiles --var var.Src --directory-ref INSTALLDIR > files.wxs
wixl -D Src=$M/SieuHoc -o SieuHoc_$V.msi main.wxs files.wxs 2>/dev/null
mkdir -p /home/user/BO_CAI
cp $ST/SieuHoc_Setup_$V.exe /home/user/BO_CAI/SieuHoc_Setup_$V.exe
cp $M/SieuHoc_$V.msi /home/user/BO_CAI/SieuHoc_$V.msi
cp /home/user/TOEIC_APP/SieuHocTOEIC.html /home/user/BO_CAI/SieuHoc_offline.html
ls -la /home/user/BO_CAI
