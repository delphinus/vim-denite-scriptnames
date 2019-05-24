# ============================================================================
# FILE: scriptnames.py
# AUTHOR: delphinus <me@delphinus.dev>
# License: MIT license
# ============================================================================

from .base import Base
from functools import reduce
from os.path import expanduser
import re


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = "scriptnames"
        self.kind = "file"
        self._re = re.compile(r"^\s*\d+:\s+(.*)$")

    def gather_candidates(self, context):
        output = self.vim.call("denite#source#scriptnames#load")

        def files(candidates, line):
            m = self._re.match(line)
            if m:
                candidates.append(
                    {
                        "word": m.group(1),
                        "abbr": line,
                        "action__path": expanduser(m.group(1)),
                    }
                )
            return candidates

        return reduce(files, output.splitlines(), [])
