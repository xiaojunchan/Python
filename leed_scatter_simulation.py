import subprocess
#cmd = 'ls'
cmd = '\"D:\\Dropbox\\MPhil Study\\Program\\Fortran\\test.exe\"'
p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
print p.stdout.read()
p.stdin.write('3/n')
print p.stdout.read()