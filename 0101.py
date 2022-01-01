def mark_html(tag):
    def outer_wrapper(function):
        def inner_wrapper(*args, **kwargs):
            return '<' + tag + '>' + function(*args, **kwargs) + '</' + tag + '>'
        return inner_wrapper
    return outer_wrapper


@mark_html('b')
def print_bold(title):
    return title


@mark_html('h1')
def print_title(title):
    return title


print(print_title('야호'))
