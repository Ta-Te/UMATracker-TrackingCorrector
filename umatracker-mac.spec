import os
import glob


DEBUG_FLAG = False
if os.getenv('UMA_DEBUG') == 'true':
    DEBUG_FLAG = True

datas = [('./data', 'data'), ('./qt/mac/qt.conf', '.')]

if os.getenv('CONDA_PREFIX'):
    PREFIX = os.getenv('CONDA_PREFIX')
else:
    PREFIX = '/usr/local/Cellar/ffms2/*'

ffms2_dlls = glob.glob(os.path.join(PREFIX, 'lib', 'libffms2.dylib'))
ffmpeg_dlls = glob.glob(os.path.join(PREFIX, 'lib', 'libavresample.[0-9].dylib'))
ffmpeg_dlls += glob.glob(os.path.join(PREFIX, 'lib', 'libswscale.[0-9].dylib'))
ffmpeg_dlls += glob.glob(os.path.join(PREFIX, 'lib', 'libavutil.[0-9][0-9].dylib'))
ffmpeg_dlls += glob.glob(os.path.join(PREFIX, 'lib', 'libavcodec.[0-9][0-9].dylib'))
ffmpeg_dlls += glob.glob(os.path.join(PREFIX, 'lib', 'libavformat.[0-9][0-9].dylib'))

binaries = [
    (x, 'lib')
    for x in ffms2_dlls
]
binaries += [
    (x, '.')
    for x in ffmpeg_dlls
]

a = Analysis(['./main.py'],
        pathex=['./'],
        binaries=binaries,
        datas=datas,
        hiddenimports=['fractions'],
        hookspath=None,
        runtime_hooks=None,
        excludes=None,
        win_no_prefer_redirects=None,
        win_private_assemblies=None,
        cipher=None)

tmp = []

lib_path_list = [
        '/usr/local/Cellar/ffmpeg/',
        '/usr/local/Cellar/x264/',
        '/usr/local/Cellar/lame/',
        '/usr/local/Cellar/libvo-aacenc/',
        '/usr/local/Cellar/geos'
        ]

for lib_path in lib_path_list:
    for dir_path, dir_names, file_names in os.walk(lib_path):
        for file_name in file_names:
            full_path = os.path.join(dir_path, file_name)
            if os.path.splitext(file_name)[1]=='.dylib':
                tmp.append(
                        (
                            file_name,
                            full_path,
                            'BINARY'
                            )
                        )
a.binaries += tmp

pyz = PYZ(a.pure, cipher=None)
exe = EXE(pyz,
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
        a.binaries,
        name='UMATracker-TrackingCorrector',
        debug=DEBUG_FLAG,
        strip=None,
        upx=True,
        console=DEBUG_FLAG, icon='./icon/icon.icns')

coll = COLLECT(exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=None,
        upx=True,
        name=os.path.join('dist', 'UMATracker'))

app = BUNDLE(coll,
        name=os.path.join('dist', 'UMATracker-TrackingCorrector.app'),
        appname="UMATracker-TrackingCorrector",
        version = '0.1', icon='./icon/icon.icns'
        )
