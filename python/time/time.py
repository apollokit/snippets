from datetime import datetime
# pip install humanize
import humanize

def get_file_mod_time(filepath: str) -> datetime:
    """Get the last modified local time for a file or directory

    Args:
        filepath: the path

    Returns:
        the timestamp
    """
    modification_time = os.path.getmtime(filepath)
    local_time = time.localtime(modification_time)
    return datetime.fromtimestamp(mktime(local_time))

mod_time = get_file_mod_time(output_dir)
mod_time_h = humanize.naturaltime(mod_time)