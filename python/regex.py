# see https://docs.python.org/2/library/re.html#re.findall
# https://stackoverflow.com/a/180993
# regular expression cheat sheet, check:
# https://ryanstutorials.net/regular-expressions-tutorial/regular-expressions-cheat-sheet.php


## Extract a specific value from some text

content = '<input type="hidden" name="atl_token" value="73813332f6383905f2e9aaa38ec59e755a312830">'
matches = re.findall(r'<input ty1pe="hidden" name="atl_token" value="(\S*)">', content)
# matches[0] is '73813332f6383905f2e9aaa38ec59e755a312830'





## Extract specific value with "or" operation

# want to extract all key-value pairs, either followed by ';' or at the end
# of the string
# a couple important things here
# - (?:;|$)
#     - (;|$) matches ; or the end of the string
#     - adding ?: tells it not to use that for match groups (https://stackoverflow.com/a/8609636)
# - \S*?
#     - \S is Anything which is not considered whitespace.
#     - *? means any number of characters, but be as short/conservative as
#             possible with the match (https://stackoverflow.com/a/11301418)
#             otherwise the "blah" match _could_ glom on with the "_octo" one
content = '_octo=GH1.1.284115065.1615783934; blah=asdfsad; has_recent_activity=1'
cookie_pairs = re.findall(r"\S*=\S*?(?:;|$)", content)
# finds
# - _octo=GH1.1.284115065.1615783934
# - blah=asdfsad
# - has_recent_activity=1






## check that a string matches a format

re.search(r'^\d{4}-\d{2}-\d{2}$', '2019-05-15')
# returns <re.Match object; span=(0, 10), match='2019-05-15'>
re.search(r'^\d{4}-\d{2}-\d{2}$', '2019-05-15g')
# returns Noneright before the movie





## find a single matching group

the_string = """"0, null, to 'pipe:':\n  Metadata:\n    major_brand     : isom\n    minor_version   : 512\n    compatible_brands: isomiso2avc1mp41\n    encoder         : Lavf58.20.100\n    Stream #0:0(eng): Video: h264 (High) (avc1 / 0x31637661), yuv420p, 848x464 [SAR 1:1 DAR 53:29], q=2-31, 1483 kb/s, 29.97 fps, 30 tbr, 30 tbn, 30 tbc (default)\n    Metadata:\n      creation_time   : 1970-01-01T00:00:00.000000Z\n      handler_name    : VideoHandler\nStream mapping:\n  Stream #0:0 -> #0:0 (copy)\nPress [q] to stop, [?] for help\nframe= 1145 fps=0.0 q=-1.0 Lsize=N/A time=00:00:38.16 bitrate=N/A speed=2.29e+03x    \nvideo:6916kB audio:0kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: unknown\n""""

out = re.search(r'frame\= ([0-9]*)\sfps', the_string)
print(out.group()) # 'frame= 1146 fps'
# groups is all the groups from the match, not multiple matches
print(out.groups()[0]) # '1146'
width_height = re.search('Video: .*, .*, ([0-9]*)x([0-9]*) ', the_string).groups()
video_width = int(width_height[0])
video_height = int(width_height[1])






## find index of first matching group

def re_search(pattern, text: str, start_indx: int = 0) -> Optional[int]:
    """Search for and return the start index of the first match for regex
    pattern.

    Simple convenience wrapper around basic regex search functions
    
    Args:
        pattern: regex pattern of type _sre.SRE_Pattern created with re.compile(r'\S')
        text: the text to seach in
        start_indx: the index within text at which to start searching
    
    Returns:
        The start index of the matched pattern, if there is a match. Otherwise,
            None
    """
    # 
    match = pattern.search(text, start_indx)
    if match is not None:
        indx = match.start()
    else:
        indx = None
    return indx

re_whitespace = re.compile(r'\s')
re_search(re_whitespace,'asdf  nliljioasfsdafio') # outputs 4
re_non_whitespace = re.compile(r'\S')
re_search(re_non_whitespace,'  nliljioasfsdafio') # outputs 2

