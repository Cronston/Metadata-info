def format_file_size(bytes_size):

    if bytes_size == 0:
        return '0 Bytes'
    
    k = 1024
    sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB']
    i = 0
    size = bytes_size
    
    while size >= k and i < len(sizes) - 1:
        size /= k
        i += 1
    
    return f"{size:.2f} {sizes[i]}"


def escape_html(text):

    if not isinstance(text, str):
        text = str(text)
    
    html_escape_table = {
        "&": "&amp;",
        '"': "&quot;",
        "'": "&apos;",
        ">": "&gt;",
        "<": "&lt;",
    }
    
    return "".join(html_escape_table.get(c, c) for c in text)


def format_pdf_date(date_string):

    if not date_string:
        return 'N/A'
    
    if date_string.startswith('D:') and len(date_string) >= 16:
        try:
            year = date_string[2:6]
            month = date_string[6:8]
            day = date_string[8:10]
            hour = date_string[10:12]
            minute = date_string[12:14]
            
            return f"{year}-{month}-{day} {hour}:{minute}"
        except (IndexError, ValueError):
            return date_string
    
    return date_string
