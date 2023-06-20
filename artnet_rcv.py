from socket import *
#import numpy as np

host = '127.0.0.1' # 送信元IPアドレス
universe = 0 # universe番号

class udprecv():
    def __init__(self):
        
        
        # ipアドレスを取得、表示
        SrcIP  = gethostbyname(gethostbyname(host))
        SrcPort = 6454                                 # 受信元ポート番号
        self.SrcAddr = (SrcIP, SrcPort)                # アドレスをtupleに格納
        self.BUFSIZE = 1024                            # バッファサイズ指定
        self.udpServSock = socket(AF_INET, SOCK_DGRAM) # ソケット作成
        self.udpServSock.bind(self.SrcAddr)            # 受信元アドレスでバインド

    def recv(self):
        packe,addr=self.udpServSock.recvfrom(self.BUFSIZE)
        data = [int(b) for b in packe]
        #del data[0:18]
        if data[14] == universe:
            del data[0:18]
            print(data)

udp = udprecv()
while True:
    udp.recv()
