
This is a script I used to transcode, deinterlace and upscale some mini DV tapes I had using *VapourSynth* and *ffmpeg-python*


This was a project I'd been thinking about for years, ripping some miniDV tapes I had recorded from 2001, when I bought a [Sony DCR-PC110](https://www.videomaker.com/article/c5/8210-sony-digital-camcorder-review-dcr-pc110-mini-dv), until about 2009 when it stopped working.

To do the task, I bought a second hand mini dv camcorder with firewire (not all of these camcorders had firewire digital transfer capablility) and a firewire pci card for my workstation.  Then I ripped them, one at a time 20x.  These transfer in real time, so an hour each.  I totally forgot how long it takes to rewind tapes.  The software for this was not as straight forward as I thought.  I remembered that Premier Pro could do this, but I couldn't get that to work.  I ended up using [this](http://www.scenalyzer.com/), after finding the author replying to someone with my same issue.  It worked fine.  A couple of my tapes transferred with lots of static and it had some trouble detecting NTSC sometimes, but retrying worked.

After all the rips, I had 1300+ clips all in folders from the tape name.  These come in as AVI files with the DVCPRO codec.  I wanted to deinterlace these and have them as h264 files so I set about making a script to do this.

I stared with ffmpeg, but found lots of people on the internet pointing to QTGMC as the preferred choice for deinterlacing.  This sent me down a rabbit hole where I learned all about [AviSynth](http://avisynth.nl/index.php/Main_Page) and the Doom9 and videohelp forums.  While reading up on AviSynth and searching things to get it working, I kept seeing references to [VapourSynth](https://www.vapoursynth.com/).  It wasn't until I had something working in AviSynth and began to consider how I could write some python to do it in batch did I realize what VapourSynth was all about.  It'ss a re-working of AviSynth for the modern world and in python.  So I started digging into this.  This was not exactly starting over, but was close.  [This guy](https://macilatthefront.blogspot.com/2018/12/using-vapoursynth-for-qtgmc-round-one.html) has a blog that I used for clues, first for AviSynth, then for VapourSynth.  Collecting all the bits and getting the right versions aligned was a project and eventually I got there.

I used a conda environment for collecing all my bits.  The script above is using [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) to get the encoding done right in the script, which I thought would be better then the 'vspipe.exe' which was widely referenced.  I knew there would be some way to pipe into ffmpeg right in the script but I didn't see anyone doing this.  I found [this post](https://forum.videohelp.com/threads/392480-Easy-way-to-encode-vpy-scripts#post2544851) which had the clues that got me there in the end (with some trial and error).  I am glad I went this route, I'm sure this pipe-to-ffmpeg-python will be something I use again.

This script above is what I used to encode my movie files.  I'm not an expert and there may be better options for better visuals or faster encoding, but this is what I went with.  I encoded with NVEnc and was seeing 28fps encoding typically.  My process ran for a few days.  If I were to do it again, I'd put in some logging.  I hope this is helpful for someone