import subprocess
import time
from ..testes import teste # funcionou com o comando$ python3 -m projeto001.source.main

print(__package__)
print(__name__)


args_flask = ["python3", "-m", "projeto001.source.servers.flask_server"]
#args_flask_shell = ["python3 -m projeto001.source.servers.flask_server"]
args_http = ["python3", "-m", "http.server", "--directory", "./frontend/static"]



#cwd=None, parametro de popen, muda o diretorio de trablho antes de executar o processo filho
flask_server = subprocess.Popen(args_flask, start_new_session=True )
time.sleep(10)
print("Pid flask: ", flask_server.pid)



#http_server = subprocess.Popen(args_http)
#print("Pid http: ", http_server.pid)


#flask_server.poll())	
#flask_server.terminate()
#flask_server.wait(Timeout) -> returncode or TimeoutExpired
#flask_server.kill()
#flask_server.communicate(AnyString, Timeout) -> Tuple(AnyString, AnyString)
#flask_server.send_signal(sig: int) -> None
#flask_server.returncode
#flask_server.stdin
#flask_server.stdout
#flask_server.stderr