import subprocess

def run_command(c):
    cmds = c.split()
    return subprocess.Popen(cmds, stdout=subprocess.PIPE).communicate()[0]

def get_brightness():
    r = run_command('screenbrightness -l')
    r = r.split('brightness ')[-1]
    return float(r)

def save_current_brightness():
    b = get_brightness()
    with open('brightness.txt', 'w') as f:
        f.write(str(b))
def get_last_brightness():
    t = None
    with open('brightness.txt', 'r') as f:
        t = f.read()
    return float(t)

c = get_brightness()
if c < 0.001:
    run_command('screenbrightness {0}'.format(get_last_brightness()))
else:
    save_current_brightness()
    run_command('screenbrightness 0')
