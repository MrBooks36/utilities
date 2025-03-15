def compressall(where="c:/", output=False, compress=True):
    import os
    import subprocess
    matches = []
    for root, dirnames, filenames in os.walk(where, topdown=True):
         for filename in filenames:
                if os.path.exists(os.path.join(root, filename)):
                   command = f'compact /c "{filename}"' if compress else f'compact /u "{filename}"'
                   subprocess.run(command, capture_output=True)
                   if output:
                    print(os.path.join(root, filename))