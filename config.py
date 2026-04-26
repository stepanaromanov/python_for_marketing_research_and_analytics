# ============================================================
# Portfolio-wide visualisation config
# Import in every notebook: from config import *
# ============================================================

# Okabe-Ito (Wong 2011, Nature Methods) — colorblind-safe
PALETTE_CATEGORICAL = [
    '#0072B2',  # blue
    '#E69F00',  # orange
    '#009E73',  # green
    '#CC79A7',  # pink
    '#56B4E9',  # sky blue
    '#D55E00',  # vermillion
    '#F0E442',  # yellow (use sparingly on white bg)
    '#333333',  # near-black
]

PALETTE_SEQUENTIAL = 'Viridis'
PALETTE_DIVERGING  = 'RdYlGn'
PLOTLY_TEMPLATE    = 'plotly_white'

# Convenience aliases
C_BLUE       = '#0072B2'
C_ORANGE     = '#E69F00'
C_GREEN      = '#009E73'
C_PINK       = '#CC79A7'
C_SKY        = '#56B4E9'
C_VERMILLION = '#D55E00'
C_YELLOW     = '#F0E442'
C_GRAY       = '#888780'
C_POSITIVE   = '#1A9850'  # RdYlGn dark green
C_NEGATIVE   = '#D73027'  # RdYlGn dark red
C_NEUTRAL    = '#888780'

FONT_FAMILY  = 'system-ui, -apple-system, sans-serif'
