from .colors import colors
from .label_positions import LOWER_RIGHT


ops = {
    # node style
    'NODE_TRANSPARENCY': 255,
    'NODE_SIZE': 25,
    'NODE_BORDER_WIDTH': 4,
    'NODE_BORDER_PAINT': colors.BRIGHT_GREEN,
    'NODE_FILL_COLOR': colors.DARK_GREEN,
    'NODE_SELECTED_PAINT': colors.BRIGHT_YELLOW,

    # node label style
    'NODE_LABEL_COLOR': colors.BRIGHT_GRAY,
    'NODE_LABEL_FONT_SIZE': 16,
    'NODE_LABEL_POSITION': LOWER_RIGHT,

    # edge style
    'EDGE_TRANSPARENCY': 255,
    'EDGE_WIDTH': 2.5,
    'EDGE_LINE_TYPE': 'SOLID',
    'EDGE_STROKE_SELECTED_PAINT': colors.BRIGHT_YELLOW,
    'EDGE_STROKE_UNSELECTED_PAINT': colors.BRIGHT_GRAY,
    'EDGE_TARGET_ARROW_UNSELECTED_PAINT': colors.BRIGHT_GRAY,
    'EDGE_TARGET_ARROW_SHAPE': 'DELTA',

    # network style
    'NETWORK_BACKGROUND_PAINT': colors.DARK_GRAY
}
