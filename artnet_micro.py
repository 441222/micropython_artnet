from socket import *
import machine, neopixel

np = neopixel.NeoPixel(machine.Pin(10), 170)

class udprecv():
    def __init__(self):
        # ホスト名を取得、表示
        # host = gethostbyname(gethostname())
        host = '127.0.0.1'
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
        del data[0:18]
        print(data)
        
        for i in range(170):
            np[i] = (data[i*3], data[i*3+1], data[i*3+2])
            np.write()

udp = udprecv()
while True:
    udp.recv()
