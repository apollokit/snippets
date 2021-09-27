import traceback
from typing import Tuple

def getStackInfo(stack_index: int = 0) -> Tuple[str, int, str, str]:
    """Get info about a specific frame in the python execution stack.

    Basically, given a stack frame index, return information about the python 
    code line currently executing in that stack frame

    Args:
        stack_index: which index into stack. 0 is top of stack, 1 is next frame 
            below, 2 below that, etc.

    Returns:
        tuple of: filename, line number, function name, line string
    """
    # map from custom stack index above to an index in the stack list
    # need to subtract one because this function counts as a frame as well
    stack_index = -1*stack_index - 1
    stack = traceback.extract_stack()
    frame_summary = stack[stack_index]
    lineno = frame_summary.lineno
    filename = frame_summary.filename
    line_str = frame_summary.line
    function_name = frame_summary.name
    return filename, lineno, function_name, line_str 