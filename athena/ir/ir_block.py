from collections import namedtuple

Block = namedtuple(
    "Block",
    [
        "owner_op",
        "is_entry_block",
        "region_idx",
        "block_idx",
        "block_func",
        "free_vars",
        "args",
    ],
)
