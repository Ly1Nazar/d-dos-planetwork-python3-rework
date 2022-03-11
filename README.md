# D-Dos
<hr>
Rework of Planetwork-DDOS author: https://github.com/Hydra7/Planetwork-DDOS
added a switch for number of packages sent and fixed the use via python3 
<h1>Usage:</h1>
<h6><p>1)&nbsp;Previously: You will need to install <a href="https://nmap.org/download.html">nmap</a> </p></h6>
<p>1)&nbsp;open cmd</p>
<p>python planet.py &lt;local ip of device&gt; &lt;open port of router&gt; &lt;number of packages&gt;</p>
<p>2)&nbsp; &lt;local ip of device&gt; usually = 192.168.0.1 / 192.168.1.1 &emsp;check via "ipconfig"</p>
<p>3)&nbsp;get website ip and open port:</p>
    <p>&emsp;&emsp;&emsp;3a)&nbsp;get &lt;target ip&gt via nmap for i.e. type in cmd: nmap example.com</p>
    <p>&emsp;&emsp;&emsp;3d)&nbsp;in summary choose one of the open ports</p>
<p>4)&nbsp;and choose the number of packets number which will be multiplied by 1000</p>
<h4>
<p>command in cmd will look like:</p></h4>
<h3><p>python planet.py 192.168.0.1 80 99</p></h3>
