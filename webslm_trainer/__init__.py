# SPDX-License-Identifier: Apache-2.0
"""WebSLM Trainer entry points.

The training engine remains in the upstream ``unsloth`` namespace so existing
models, integrations, and examples continue to work.
"""

from importlib import import_module


def __getattr__(name: str):
    return getattr(import_module("unsloth"), name)
