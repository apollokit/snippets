# https://stackoverflow.com/a/180993

the_string = """"0, null, to 'pipe:':\n  Metadata:\n    major_brand     : isom\n    minor_version   : 512\n    compatible_brands: isomiso2avc1mp41\n    encoder         : Lavf58.20.100\n    Stream #0:0(eng): Video: h264 (High) (avc1 / 0x31637661), yuv420p, 848x464 [SAR 1:1 DAR 53:29], q=2-31, 1483 kb/s, 29.97 fps, 30 tbr, 30 tbn, 30 tbc (default)\n    Metadata:\n      creation_time   : 1970-01-01T00:00:00.000000Z\n      handler_name    : VideoHandler\nStream mapping:\n  Stream #0:0 -> #0:0 (copy)\nPress [q] to stop, [?] for help\nframe= 1145 fps=0.0 q=-1.0 Lsize=N/A time=00:00:38.16 bitrate=N/A speed=2.29e+03x    \nvideo:6916kB audio:0kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: unknown\n""""

import re

out = re.search('frame\= ([0-9]*)\sfps', the_string)
print(out.group()) # 'frame= 1146 fps'
print(out.groups()[0]) # '1146'
width_height = re.search('Video: .*, .*, ([0-9]*)x([0-9]*) ', the_string).groups()
video_width = int(width_height[0])
video_height = int(width_height[1])
