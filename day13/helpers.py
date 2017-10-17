import io
from contextlib import redirect_stdout


def get_print_output(testowana_funkcja, a, b):

    bufor_pamieci = io.StringIO()

    with redirect_stdout(bufor_pamieci):

        testowana_funkcja(a, b)

        return bufor_pamieci.getvalue()
