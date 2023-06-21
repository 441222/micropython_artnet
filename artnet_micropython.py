import usocket as socket
import machine, neopixel

host = '127.0.0.1' # 送信元IPアドレス
universe = 0 # universe番号

total = 240 #ledの数
led_num = 3 #何こづつ制御するか

np = neopixel.NeoPixel(machine.Pin(10), total) #neopixelの設定


class udprecv():
    def __init__(self):
        SrcIP  = gethostbyname(gethostbyname(host))    # 送信元IPアドレス
        SrcPort = 6454                                 # 受信元ポート番号
        self.SrcAddr = (SrcIP, SrcPort)                # アドレスをtupleに格納
        self.BUFSIZE = 1024                            # バッファサイズ指定
        self.udpServSock = socket(AF_INET, SOCK_DGRAM) # ソケット作成
        self.udpServSock.bind(self.SrcAddr)            # 受信元アドレスでバインド

    def recv(self):
        packe,addr=self.udpServSock.recvfrom(self.BUFSIZE) #受信
        data = [int(b) for b in packe] #byte型をint型に変換

        try:
            if data[14] == universe:       #universe番号が一致したらneopixelに送信
                del data[0:18]
                print(data)
                for i in range(total/led_num): 
                    for j in range(led_num):
                        np[i*led_num+j] = (data[i*led_num+j*3], data[i*led_num+j*3+1], data[i*led_num+j*3+2]) 
                np.write()
        except IndexError:
            pass

udp = udprecv()
while True:
    udp.recv()
