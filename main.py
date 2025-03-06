from doc_processing import add_page_num
from formatting import clear_formatting, format_text, remove_style_borders

# Global page count
page_count = 1

# 1) Add "[Slide x]" markers and copy document content
page_count = add_page_num("./tests/test_file.docx", "./tests/final-result.docx", page_count)

# 2) Clear all formatting
clear_formatting("./tests/final-result.docx", "./tests/final-result.docx")

# 3) Apply custom formatting
format_text("./tests/final-result.docx", "./tests/final-result.docx")

# 4) Remove border from the specified style (e.g., "Title")
remove_style_borders("./tests/final-result.docx", "./tests/final-result.docx", "Title")