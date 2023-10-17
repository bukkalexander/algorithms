import shutil
import subprocess
import threading

def remove(path):
    if not path.exists():
        return
    if path.is_dir:
        shutil.rmtree(path)
    else:
        path.unlink()
    print(f"removed: {path}")


def run(commands, shell=False, cwd=None, env=None):
    """
    Wrapper of subprocess.Popen configured to combine STDOUT and STDERR to a single
    output stream that is printed continuously to the console and also returned together
    with the return code of the executed commands.

    Args:
        commands: commands to run in subprocess call
        shell: if commands should be executed in shell
        cwd: the current directory before subprocess call executes
        env: the environment variables for the subprocess call

    Returns:
        return_code, stdout, stderr, output (combined stdout and stderr)

    Example
    --------
        >>> cmd = ["grep", "-r", "text", "/sys/"]
        >>> return_code, stdout, stderr, output = run_subprocess(cmd)

    Recommendation
    --------
        Only use `shell=True` if your `commands` are not a program with arguments
        that can be run without using a shell! This is in general more secure,
        faster, and platform independent.
    """

    universal_newlines = False  # False gives binary text mode. We decode ourselves.
    bufsize = -1

    stdout = []
    stderr = []
    output = []  # Combined stdout and stderr in the order the buffers are flushed (printed)

    with subprocess.Popen(
        commands,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd,
        env=env,
        shell=shell,
        bufsize=bufsize,
        universal_newlines=universal_newlines,
    ) as process:

        def print_and_save_stream_output(stream, stream_output, combined_stream_output, thread_lock):
            for line in stream:
                try:
                    line = bytes.decode(line)
                except:
                    line = str(line)
                print(line, end="")

                stream_output.append(line)

                with thread_lock:
                    combined_stream_output.append(line)

        # Thread lock for ensuring the combined output list isn't accessed simultaneously
        thread_lock = threading.Lock()

        # Create threads to separately print and save output to both separate and combined stream output variables
        stdout_thread = threading.Thread(
            target=print_and_save_stream_output,
            args=(process.stdout, stdout, output, thread_lock),
        )
        stderr_thread = threading.Thread(
            target=print_and_save_stream_output,
            args=(process.stderr, stderr, output, thread_lock),
        )

        # Start processing the commands and streams
        stdout_thread.start()
        stderr_thread.start()

        # Wait for threads to be done with their work e.g. join
        stdout_thread.join()
        stderr_thread.join()

    # Wait for process to finish to get return code
    return_code = process.poll()
    return return_code, "".join(stdout), "".join(stderr), "".join(output)