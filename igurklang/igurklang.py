from ipykernel.kernelbase import Kernel
from gurklang.repl import Repl
import gurklang.repl as r
from pygments.lexers import load_lexer_from_file
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO

load_lexer_from_file('lexer.py', 'GurkLexer')

def make_erroring(f):
    def fun(*args, **kwargs):
        f(*args, **kwargs)
        raise RuntimeError
    return fun



r._display_runtime_error = make_erroring(r._display_runtime_error)
r._display_parse_error = make_erroring(r._display_parse_error)


class EchoKernel(Kernel):
    implementation = 'py-gurklang'
    implementation_version = '0.1'
    language = 'gurklang'
    language_version = '0.1'
    language_info = {
        'name': 'gurklang',
        'mimetype': 'text/gurklang',
        'file_extension': '.gurk',
    }
    banner = "Gurklang - \N{CUCUMBER}"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repl = Repl()

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        stdout = StringIO()
        stderr = StringIO()
        with redirect_stderr(stderr), redirect_stdout(stdout):
            try:
                self.repl._process_command(code)
            except RuntimeError:
                status = 'error'
            else:
                status = 'ok'

        if not silent:
            if stdout.getvalue():
                stream_content = {'name': 'stdout', 'text': stdout.getvalue()}
                self.send_response(self.iopub_socket, 'stream', stream_content)
            if stderr.getvalue():
                stream_content = {'name': 'stderr', 'text': stderr.getvalue()}
                self.send_response(self.iopub_socket, 'stream', stream_content)
        return {'status': status,
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=EchoKernel)
