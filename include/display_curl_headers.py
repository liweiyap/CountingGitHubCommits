import pycurl


curl_headers = {}

def display_curl_headers(header_line):
    """
    Optional header function for PycURL object.
    
    Args:
        header_line: byte string containing information for headers.
    
    Returns:
        Either None or no. of bytes written/displayed.
    """
    header_line = header_line.decode('iso-8859-1')
    if ':' not in header_line:
        return
    header_name, header_value = header_line.split(':', 1)
    header_name = header_name.strip()
    header_value = header_value.strip()
    header_name = header_name.lower()
    curl_headers[header_name] = header_value
