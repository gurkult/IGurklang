from ipykernel.kernelbase import Kernel
import sys
sys.path.append('gurklang')
from gurklang.repl import Repl
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO

class EchoKernel(Kernel):

    implementation = 'Echo'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {
        'name': 'Any text',
        'mimetype': 'text/plain',
        'file_extension': '.txt',
    }
    banner = "Echo kernel - as useful as a parrot"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repl = Repl()

    def do_run(self, code):
        self.repl._process_command(code)

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        stdout = StringIO()
        stderr = StringIO()
        with redirect_stderr(stderr), redirect_stdout(stdout):
            self.do_run(code)

        if not silent:
            if stdout.getvalue():
                stream_content = {'name': 'stdout', 'text': stdout.getvalue()}
                self.send_response(self.iopub_socket, 'stream', stream_content)
            if stderr.getvalue():
                stream_content = {'name': 'stderr', 'text': stderr.getvalue()}
                self.send_response(self.iopub_socket, 'stream', stream_content)
        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=EchoKernel)
