import plotly.graph_objects as go

# ── Shared visual style ────────────────────────────────────────────────────────
PALETTE = {
    "primary":    "#4C6EF5",   # indigo  – main data series
    "secondary":  "#F76707",   # orange  – comparison / highlight series
    "accent":     "#2F9E44",   # green   – annotations, positive signals
    "muted":      "#868E96",   # gray    – reference lines, axes helpers
    "background": "#F8F9FA",   # light gray canvas
    "surface":    "#FFFFFF",   # white   – plot area
}

FONT = {
    "family": "Inter, Arial, sans-serif",
    "size_title":  18,
    "size_axis":   13,
    "size_tick":   11,
    "size_legend": 12,
}

def base_layout(title="", xaxis_title="", yaxis_title=""):
    """Return a Plotly Layout with the shared style applied."""
    return go.Layout(
        title=dict(text=title, font=dict(size=FONT["size_title"], family=FONT["family"])),
        xaxis=dict(
            title=xaxis_title,
            title_font=dict(size=FONT["size_axis"]),
            tickfont=dict(size=FONT["size_tick"]),
            gridcolor="#DEE2E6",
        ),
        yaxis=dict(
            title=yaxis_title,
            title_font=dict(size=FONT["size_axis"]),
            tickfont=dict(size=FONT["size_tick"]),
            gridcolor="#DEE2E6",
        ),
        legend=dict(font=dict(size=FONT["size_legend"])),
        paper_bgcolor=PALETTE["background"],
        plot_bgcolor=PALETTE["surface"],
        margin=dict(l=60, r=30, t=60, b=60),
    )
