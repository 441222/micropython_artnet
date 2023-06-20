from socket import *
import machine, neopixel

host = '127.0.0.1' # 送信元IPアドレス

total = 240 #ledの数
led_num = 3 #何こづつ制御するか

np = neopixel.NeoPixel(machine.Pin(10), total)


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
        del data[0:18]
        print(data)
        
        for i in range(total/led_num):
            for j in range(led_num):
                np[i*led_num+j] = (data[i*led_num+j*3], data[i*led_num+j*3+1], data[i*led_num+j*3+2])
        np.write()

udp = udprecv()
while True:
    udp.recv()
