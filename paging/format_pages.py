def format_pages(current_page, total_pages):
    output = ''
    for i in range(1, total_pages+1):
        if i == current_page:
            output += f'({i}) '
        else:
            output += f'{i} '
    return output.rstrip()
