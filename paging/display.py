class Pages:
    def __init__(self, **kwargs):
        self.selected_page = kwargs['selected']
        self.total_pages = kwargs['total']

    def display(self):
        def format_page_number(p):
            selected_page_number = f'({p})'
            regular_page_number = f'{p}'
            return selected_page_number if p == self.selected_page else regular_page_number

        formatted_pages = [format_page_number(p) for p in range(1, self.total_pages + 1)]
        return ' '.join(formatted_pages)
