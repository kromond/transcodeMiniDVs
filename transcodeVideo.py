## set the in and out path variables
## run this script from the conda env called: vapoursynthEnv

from pathlib import Path
import ffmpeg
import vapoursynth as vs
import adjust as adj
import havsfunc as haf
import sys

core = vs.core

inpath = Path("Y:\\MiniDV_circa2001-2009")
outpath = Path("Y:\\MiniDV_circa2001-2009_mp4")

files = [x for x in inpath.glob('**/*.avi') if x.is_file ]
# print("Running on these files:")
# for x in files:
#     print(x)

for idx, x in enumerate(files):
    print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| >> Working on file: %s of %s files' % (idx+1,  len(files)))
    source = x  # this is the full filename.avi
    destDir = outpath / x.parent.name
    destDir.mkdir(parents=True, exist_ok=True)
    dest = str(source).replace('.avi', '_720p.mp4')
    dest = dest.replace(str(inpath), str(outpath))
    print("source: %s" % source)
    print("dest: %s" % dest)

    clip = core.ffms2.Source(source=str(source))
    clip = core.std.SetFrameProp(clip, prop="_Matrix", intval=6)
    clip = core.resize.Bicubic(clip, format=vs.YUV420P8, matrix_s="709") # reformat clip
    clip = haf.QTGMC(clip, Preset='Medium', Sharpness=0.75, EZDenoise=5, NoisePreset="Slow", ChromaNoise=True, TFF=False)
    #clip = core.text.FrameProps(clip)
    clip = adj.Tweak(clip, sat=1.25) # bump some saturation
    clip = core.resize.Bicubic(clip, 1280, 960)

    v1 = ffmpeg.input('pipe:', thread_queue_size=1024)
    a1 = ffmpeg.input(source).audio
    out = ffmpeg.output(v1, a1, dest, vcodec='h264_nvenc', preset='p7', tune='hq', rc='vbr', cq=19, pix_fmt='yuv420p').overwrite_output()
    process = out.run_async(pipe_stdin=True)

    clip.output(process.stdin, y4m = True)  # should y4m be True?
    process.communicate()
