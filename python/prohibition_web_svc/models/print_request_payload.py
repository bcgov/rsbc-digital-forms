from typing import TypedDict, Optional, Dict, Any


class PrintOptions(TypedDict, total=False):
    """Options for print rendering."""
    type: str  # 'pdf' or 'html'
    filename: str


class PrintRequestPayload(TypedDict, total=False):
    """Request payload for print/render operations."""
    template: str  # Template name/path
    data: Dict[str, Any]  # Template data
    options: PrintOptions  # Rendering options
