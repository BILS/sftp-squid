from paramiko.transport import Transport
from paramiko.rsakey import RSAKey
from paramiko.sftp_client import SFTPClient


key = RSAKey.from_private_key_file(filename="/Users/johanviklund/Work/sftp-squid/vm/.vagrant/machines/default/virtualbox/private_key")

window_size = 2**21
packet_size = 2**15

#window_size = 2**31
#packet_size = 2**21

tr = Transport(('localhost', 2222), default_window_size=window_size, default_max_packet_size=packet_size)
tr.connect(username='vagrant', pkey=key)


#sftp = SFTPClient.from_transport(tr, window_size=2**21, max_packet_size=2**15)
sftp = SFTPClient.from_transport(tr, window_size=window_size, max_packet_size=packet_size)

print("Transferring test_file")
sftp.put('test_file', 'test_file')
print("Done")

tr.close()
