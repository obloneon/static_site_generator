from enum import Enum


class BlockType(Enum):
      PARAGRAPH = "paragraph"    
      HEADING = "heading"    
      CODE = "code"
      QUOTE = "quote"    
      ULIST = "unordered_list"    
      OLIST = "ordered_list"  


# Takes a raw Markdown string (representing a full document) as input and returns a list of "block" strings.
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


# Takes a single block of markdown text as input and returns the BlockType representing the type of block it is.
def block_to_block_type(block):
    block_lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(block_lines) > 1 and block_lines[0].startswith("```") and block_lines[-1].startswith("```"):
        return BlockType.CODE
    is_quote = True
    is_unordered_list = True
    is_ordered_list = True
    for i in range(len(block_lines)):
        line = block_lines[i]
        if not line.startswith(">"):
            is_quote = False
        if not line.startswith("- "):
            is_unordered_list = False
        if not line.startswith(f"{i + 1}. "):
            is_ordered_list = False
    if is_quote:
        return BlockType.QUOTE
    if is_unordered_list:
        return BlockType.ULIST
    if is_ordered_list:
        return BlockType.OLIST
    return BlockType.PARAGRAPH
